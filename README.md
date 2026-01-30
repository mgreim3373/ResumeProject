# ATS Resume Coach

An AI-powered resume optimization tool that analyzes your resume against job postings, suggests improvements, and grades your revisions in real-time.

## Overview

This tool uses Claude AI to coach you through optimizing your resume for Applicant Tracking Systems (ATS). It provides specific suggestions and lets YOU make the edits - then grades your revisions iteratively until you're satisfied.

**Key Features:**
- Calculates ATS keyword match score against job postings
- Suggests qualifications you could add (if you have the experience)
- Suggests small text changes to existing content (keyword insertions)
- Grades your revisions and shows score improvement
- Iterates until you're satisfied with your score

## Setup

### 1. Install Claude Code

This tool runs as a Claude Code slash command. Install Claude Code if you haven't already.

### 2. Create Your Base Resume

Create a file called `ORIGINAL_RESUME.txt` in this directory with your current resume text. This is your base resume that the tool will analyze.

```
ORIGINAL_RESUME.txt
```

This file should contain your full resume text - the tool will read from it automatically.

### 3. Add Job Descriptions

Save job postings as `.txt` files in this directory (e.g., `backend_job.txt`, `frontend_job.txt`).

## Usage

```bash
/resume job_description.txt
```

The tool will:
1. Read your `ORIGINAL_RESUME.txt`
2. Read the job description file you specified
3. Calculate your current ATS score
4. Provide improvement suggestions

## How It Works

```
1. You run /resume with a job posting file
2. Claude reads ORIGINAL_RESUME.txt + job posting
3. Claude calculates your ATS score
4. Claude suggests:
   - Qualifications to ADD (new skills/experience)
   - Text changes to EXISTING content
5. You make changes and paste updated resume text in chat
6. Claude grades new version, shows improvement
7. Repeat until you type "done"
```

## Example Session

```
> /resume backend_job.txt

═══════════════════════════════════════════════════
ATS KEYWORD ANALYSIS
═══════════════════════════════════════════════════

Current Score: 18/25 keywords matched (72%)

MATCHED KEYWORDS:
✓ React, TypeScript, AWS, Docker, Kubernetes, microservices...

MISSING KEYWORDS:
✗ GraphQL, full stack, CI/CD, frontend, system integration...

═══════════════════════════════════════════════════
QUALIFICATIONS YOU COULD ADD
(if you have this experience)
═══════════════════════════════════════════════════

1. GraphQL
   → Add to skills if you've used it
   → Mention in a bullet if you've integrated GraphQL APIs

2. Customer Collaboration
   → Add experience working directly with customers

═══════════════════════════════════════════════════
SMALL TEXT CHANGES TO BOOST SCORE
═══════════════════════════════════════════════════

1. Add "full-stack" to your title
   Current: "Lead Mission Engineer..."
   Suggested: "Lead Full-Stack Mission Engineer..."
   Keyword: full stack (+1 match)

2. Add "CI/CD" alongside "GitLab CI"
   Current: "...implementing GitLab CI pipelines..."
   Suggested: "...implementing GitLab CI/CD pipelines..."
   Keyword: CI/CD (+1 match)

═══════════════════════════════════════════════════
READY TO GRADE YOUR REVISIONS
═══════════════════════════════════════════════════

Paste your updated resume text below.
Type "done" when you're finished optimizing.

> [User pastes updated resume text directly in chat]

═══════════════════════════════════════════════════
UPDATED ATS SCORE
═══════════════════════════════════════════════════

Previous Score: 18/25 (72%)
New Score:      23/25 (92%) ⬆️ +20%

NEWLY MATCHED:
+ full stack
+ CI/CD
+ frontend
+ high-performance
+ system integration

STILL MISSING:
✗ GraphQL (not in your experience)

Great improvement! Paste another revision or type "done".

> done

═══════════════════════════════════════════════════
FINAL ATS ANALYSIS
═══════════════════════════════════════════════════

Final Score: 23/25 keywords (92%)

Your resume is well-optimized for this position!
```

## Key Principles

### 1. You Make the Edits
Claude coaches and grades - you decide what changes to make. This keeps you in control of your resume's voice and content.

### 2. No Fabrication
Only add skills and experience you genuinely have. Claude will suggest opportunities but never fabricate qualifications.

### 3. Iterative Improvement
Paste as many revisions as you want. Each revision gets scored and compared to the previous version.

### 4. Specific Suggestions
Every suggestion includes:
- The exact keyword to add
- Where to add it (which section/bullet)
- Before/after example text
- Expected score impact

## Tips for High ATS Scores

1. **Match exact phrasing** - Use the same terms as the job posting (e.g., "CI/CD" not just "continuous integration")

2. **Include both forms** - Add acronyms AND full names (e.g., "Kubernetes (K8s)")

3. **Front-load keywords** - Put important keywords in your summary and skills sections

4. **Be specific** - "React, TypeScript, AWS" beats "modern web technologies"

5. **Don't stuff** - Keywords should fit naturally in context

## File Structure

```
project/
├── README.md                          # This file
├── ORIGINAL_RESUME.txt                # Your base resume (create this!)
├── .claude/skills/resume/skill.md     # Claude Code skill definition
├── sample_job.txt                     # Example job description
└── (your job files)
    └── backend_job.txt                # Job postings to optimize for
```

## License

Free to use and modify for personal use.

## Credits

Built using Claude Code.
