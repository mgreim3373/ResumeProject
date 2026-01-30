---
name: resume
description: Generate a tailored resume from master resume data and a job description. Use when the user asks to create, build, or generate a resume for a specific job.
argument-hint: [job-description-file] [resume-data-json]
allowed-tools: Read, Write, Edit, Bash, Glob, WebSearch, AskUserQuestion
---

# Resume Builder

Build a tailored resume from structured master resume data and a job description.

**CORE PHILOSOPHY:**
- **PRESERVE the user's original resume text as much as possible**
- **MINIMIZE rewrites** - only make targeted keyword insertions where needed
- **ASK the user about gaps** before generating the final resume
- **Keep ALL bullets by default** - only cut if absolutely necessary for one-page fit

**IMPLEMENTATION APPROACH:**
- **YOU (Claude Code) do ALL the AI work** - analysis, scoring, optimization
- **Python script (create_resume.py) does ONLY formatting** - converts JSON to .docx
- **NO external API calls needed** - you're already here doing the work!

## When invoked with arguments:
- First argument: Path to job description file (e.g., example_job.txt)
- Second argument (optional): Path to master resume JSON (defaults to master_resume.json)

## Steps to follow:

### 1. Read Input Files
- Read the job description file
- Read master resume JSON (default: `master_resume.json`)
- **File naming:** Derive output name from job file (e.g., `backend_job.txt` → `backend_job_resume.docx`)
- **Error handling:** If files don't exist or JSON is malformed, tell user and stop

### 2. Job Analysis & Gap Identification
Extract from job posting: required skills, preferred skills, ATS keywords (25-40 terms).

Compare against master resume and identify gaps. Present gap analysis to user in a table.

### 3. Ask User About Gaps
For each of top 40 missing skills:
1. Ask: "Do you have experience with [skill]?"
2. If yes: "Which company/role? How did you use it?"
3. Auto-apply the keyword insertion to the relevant bullet (add to skills section too)

If user has no experience, proceed without it (don't fabricate).

### 4. ATS Keyword Optimization
As many keyword insertions as possible that could boost ATS score (synonyms → exact phrasing, missing keywords that fit naturally).

Auto-apply all optimizations (exact casing matches, synonym replacements, keyword insertions). No approval needed.

**ATS Score Check:** After applying optimizations, calculate the ATS score. If below 95%, run this step again to find additional keyword insertions (expand abbreviations like "DoD" → "Department of Defense", add contextual keywords like "national security", "software teams", etc.). If still below 95% after the second attempt, inform the user of the score and continue.

### 5. Generate Professional Summary
Create 2-sentence summary (max 40 words). Front-load with job title + years of experience. Pack with 5-7 top job keywords not already covered in bullets. No fabrication.

### 6. Reorder Skills Section
Reorder skills to prioritize job keywords (most relevant first). Keep all original skills. Add any new skills from gap discussion. Match job posting's exact phrasing.

### 7. Create Tailored JSON
Write `[jobname]_tailored.json` with: new summary, original contact, reordered skills, all experiences (with approved changes applied), original education.

### 8. Generate .docx Resume
Run: `python3 create_resume.py [jobname]_tailored.json [jobname]_resume.docx`

Calculate and present final ATS score: "Matched: X/Y keywords (XX%)"

### 9. One-Page Verification
Ask user to check if resume fits on one page. If overflow, request screenshot.

**When user shares screenshot:**

1. **Find orphaned words** (FIRST) - Lines with 1-3 words. Trim filler words to eliminate orphans. Never remove job keywords.
2. **Remove non-essential skills** (SECOND) - Skills not in job posting.
3. **Cut content** (LAST RESORT) - Start with oldest position, then least relevant bullets.

**Safe to remove:** "a", "the", "that", "which", "in order to", "helped to"
**Never remove:** Job keywords, metrics, leadership bullets

Get user approval, regenerate, iterate until it fits.

### 10. Final Report
Present: matched keywords (X/Y, XX%), top 10 matched keywords, remaining gaps, generated file path.

### 11. Cleanup
Delete intermediate files: `rm -f *_tailored.json`

## Key Principles

**DO:** Preserve original text, surgical keyword insertions, ask about gaps, keep all content, reorder skills for ATS.

**DON'T:** Rewrite bullets, remove content without asking, fabricate, over-optimize.
