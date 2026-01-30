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
- First argument: Path to job description file (e.g., backend_job.txt)
- Second argument (optional): Path to master resume JSON (defaults to resume_data_example.json)

## Steps to follow:

### 1. Read Input Files
- Read the job description to understand requirements
- Read the master resume data JSON containing all experiences, skills, and education
- If job file doesn't exist, create a sample one for testing

### 2. Job Analysis & Gap Identification (CRITICAL FIRST STEP)
Analyze the job description and compare against the master resume:

**Extract from job posting:**
- Required skills (10-20 specific technical skills)
- Preferred/nice-to-have skills
- Key responsibilities
- ATS keywords (25-40 keywords)
- Seniority level and role focus

**Identify gaps - skills/experience in job posting but NOT in master resume:**
- List each missing required skill
- List each missing preferred skill
- Note any experience areas mentioned in job but not covered in resume

**Present gap analysis to user in a clear table format.**

### 3. ASK USER ABOUT GAPS (Use AskUserQuestion tool)
Before proceeding, ask the user:

"I found the following gaps between your resume and the job posting. Do you have experience with any of these that we should add?"

Present options:
- List the top 3-5 most important missing skills/experiences
- Give user opportunity to provide context for each
- Ask if they want to add any of these to their resume

**If user provides additional experience:**
- Note the new information to incorporate
- User can provide brief descriptions of their experience with missing skills

**If user has no additional experience:**
- Proceed without those skills (don't fabricate)
- Note which gaps will remain

### 4. Generate Professional Summary
- Create a **2 sentence maximum** professional summary
- Front-load with job title and years of experience
- Pack with 5-7 top keywords from job description
- **ONLY use information from master resume + any new info user provided**
- **STRICT LENGTH:** Max 40 words total
- **NO FABRICATION**

### 5. Optimize Skills Section (Reorder, Don't Remove)
- **REORDER skills** to prioritize job keywords (most relevant first)
- **KEEP all original skills** - don't remove skills from master resume
- Add any new skills user mentioned in gap discussion
- Include BOTH acronyms AND full forms where the job uses them
- Match job posting's exact phrasing where possible

### 6. Bullet Text Optimization (MINIMAL CHANGES)

**PRESERVE ORIGINAL TEXT - Only make targeted insertions:**

For each bullet in the master resume:
1. **Keep the original sentence structure and wording**
2. **Only insert job keywords where they fit naturally**
3. **Don't rewrite entire bullets** - make surgical keyword additions

**Example of GOOD minimal optimization:**
- Original: "Enhanced the Air Force command and control suite by maintaining an asynchronous event management service (produce/consume/replay) using Java, Spring, RabbitMQ, and Redis"
- Optimized: "Enhanced the Air Force command and control suite by maintaining an asynchronous event-driven management service (produce/consume/replay) using Java, Spring Boot, RabbitMQ, and Redis"
- Changes: Added "event-driven", changed "Spring" to "Spring Boot" (2 small keyword insertions)

**Example of BAD over-rewriting (DON'T DO THIS):**
- Original: "Enhanced the Air Force command and control suite..."
- Over-rewritten: "Architected mission-critical event-driven microservices processing high-transaction throughput..."
- This loses the user's voice and specific details

**Keyword insertion rules:**
- Insert exact job keywords where they fit grammatically
- Prefer adding to existing phrases over replacing them
- Keep specific details (Air Force, 250k DAU, etc.) - these are valuable
- Don't remove context to make room for keywords

### 7. Bullet Titles (Light Touch)
- **Keep original bullet titles if they work**
- Only adjust titles if they're completely misaligned with job focus
- Prefer the user's terminology

### 8. Keep ALL Positions and Bullets (Default)
- **Include ALL positions from master resume by default**
- **Include ALL bullets from master resume by default**
- Only cut content if the resume exceeds one page
- If cutting is needed, start with oldest/least relevant position

### 9. Create Tailored JSON
Write a new JSON file (e.g., `backend_tailored.json`) with:
- **"summary":** New professional summary (ATS-optimized)
- **"contact":** Original contact info (unchanged)
- **"skills":** Reordered skills (+ any new skills from user input)
- **"experiences":** All experiences with lightly optimized bullets
- **"education":** Original education (unchanged)

### 10. Generate .docx Resume
- Run: `python3 create_resume.py [tailored].json [output].docx`
- Creates professionally formatted Word document

### 11. ATS Score Optimization Loop

After generating the initial resume, present keyword optimization opportunities:

#### Step 1: Research ALL Improvement Opportunities
Identify ALL opportunities for small text changes that could boost the ATS score:

**Search for opportunities:**
1. Job keywords NOT yet in resume that COULD be added truthfully
2. Places where synonyms could be swapped for exact job phrasing
3. Summary additions (if under 40 words)
4. Bullet text where keywords fit naturally

**For each opportunity, note:**
- The keyword to add
- Where it would go (which section/bullet)
- The exact text change (before → after)
- Why it's truthful (based on user's actual experience)

**Identify 5-10 highest-impact suggestions.**

#### Step 2: Present ALL Changes One-by-One (Use AskUserQuestion)
Present EVERY suggested change to the user:

"I found an opportunity to boost your ATS score. Do you approve this change?"

**Present:**
- Current text
- Proposed text (with change highlighted)
- Keyword being added

**Options:**
- "Yes, make this change"
- "No, skip this one"

**IMPORTANT:** Do NOT calculate or show score after each change. Just collect approvals.

#### Step 3: Apply ALL Approved Changes
After presenting ALL suggestions:
- Update the tailored JSON with ALL approved changes at once
- Track which changes were made

#### Step 4: Calculate Final ATS Score
Only AFTER all changes are applied, calculate the ATS score:

**Count matches for:**
- Required skills mentioned in job posting
- Preferred skills mentioned in job posting
- Key technical terms and phrases
- Industry-specific terminology

**Calculate score:**
- Count total key terms from job posting (25-40 terms)
- Count how many appear in the resume (summary, skills, bullets)
- Score = (matched terms / total terms) × 100

**Present to user:**
```
ATS Keyword Match Analysis:
- Matched: X/Y key terms
- Estimated ATS Score: XX%
```

#### Step 5: Regenerate .docx
After all ATS optimizations are complete:
- Run: `python3 create_resume.py [tailored].json [output].docx`
- Confirm regeneration to user

### 12. One-Page Verification (SCREENSHOT FEEDBACK)

After generating the .docx, tell the user:

"Please open the resume and check if it fits on one page. If it overflows, share a screenshot and I'll recommend specific fixes."

**When user shares screenshot of overflow:**

First, tell the user:
"I'll analyze this and suggest fixes. Note: I may miss some obvious opportunities - if you see a better way to shorten content without hurting your ATS score, feel free to suggest it!"

#### Step 1: Count Lines Over
- Determine exactly how many lines overflow to page 2
- This determines how aggressive fixes need to be

#### Step 2: Find Orphaned Words/Short Lines (FIRST PRIORITY)
Scan the screenshot for lines with very few words (1-3 words). These are opportunities to save a full line by trimming just a few words from the associated bullet.

**For each orphan found:**
1. Identify which bullet it belongs to
2. Look at the FULL bullet text
3. Find 2-4 words that can be removed or shortened WITHOUT losing job keywords
4. Propose a minimal rewrite that eliminates the orphan

**Example:**
- Orphan line: "...and integration testing."
- Full bullet: "...ensured system stability through rigorous TDD and integration testing."
- Fix: "...ensured stability through rigorous TDD and integration testing." (remove "system" - saves the orphan, keeps keywords)

**CRITICAL: Preserve ATS keywords when trimming!**
- Before suggesting a trim, check if any words are job keywords
- Never remove: Java, Spring Boot, Kafka, RabbitMQ, AWS, PostgreSQL, TDD, microservices, etc.
- Safe to remove: filler words, adjectives, redundant phrases
- Safe removals: "a", "the", "that", "which", "in order to", "helped to", "was able to"

#### Step 3: Remove Non-Essential Skills (SECOND PRIORITY)
If orphan fixes aren't enough, look at skills section for items NOT in the job posting:
- Check each skill against job requirements
- Remove skills with zero keyword matches (e.g., "Elasticsearch" if not in job)
- Keep ALL skills that appear in job posting

#### Step 4: Cut Content (LAST RESORT)
Only if steps 2-3 don't save enough lines:

**Cut priority (least ATS impact first):**
1. Oldest position (KAON) - least relevant, oldest
2. Second bullet from oldest remaining position - usually less impactful
3. Process-focused bullets with few technical keywords
4. Bullets for skills already well-covered elsewhere

**Never cut:**
- Bullets with high keyword density for the target job
- Leadership/mentorship bullets (if job mentions these)
- Metrics and quantifiable achievements

#### Step 5: Propose Changes & Regenerate
1. Show user exactly what you'll change and why
2. Get user approval
3. Update JSON and regenerate .docx
4. Ask user to check again: "Does it fit now? If not, share another screenshot."

#### Step 6: Iterate
Repeat screenshot review until resume fits on one page.

**Reference - Line Savings:**
| Fix Type | Typical Savings |
|----------|-----------------|
| Trim orphan (remove 2-4 words) | 1 line |
| Remove 1 non-essential skill | 0-1 line |
| Remove oldest position entirely | 3-4 lines |
| Cut one bullet | 2-3 lines |
| Shorten a long bullet by 8-12 words | 1 line |

### 13. Final ATS Score Report

After the user confirms the resume fits on one page, calculate and present the final ATS score:

**Final Report Format:**
```
✅ Resume Complete!

Final ATS Analysis:
- Matched Keywords: X/Y (XX%)
- Estimated ATS Score: XX-XX%

Strong Matches:
- [List top 10 matched keywords]

Remaining Gaps (not in your experience):
- [List any unmatched required/preferred skills]

File Generated:
- [jobname]_resume.docx
```

**Include:**
- Final keyword match count and percentage
- List of successfully matched keywords
- Any remaining gaps (skills in job posting but not in resume)
- Confirmation of generated .docx file

### 14. Cleanup

After the user confirms the resume is complete:
- Delete any `*_tailored.json` files created during this session
- Run: `rm -f *_tailored.json`
- These intermediate files are no longer needed once the .docx is finalized

## Output:
- Generate a tailored `[jobname]_resume.docx` file
- Show summary of changes made (should be minimal)
- Present ALL suggested keyword changes for user approval (no score shown until end)
- Calculate ATS score once after all changes are applied
- Request screenshot for one-page verification
- Final ATS score report with keyword match details
- Clean up intermediate `*_tailored.json` files

## Key Principles:

**DO:**
- Preserve the user's original writing style and voice
- Make surgical keyword insertions
- Ask about gaps before assuming
- Keep all content by default
- Reorder skills for ATS priority

**DON'T:**
- Rewrite entire bullets from scratch
- Remove content without asking
- Fabricate experience or metrics
- Change the user's specific details and achievements
- Over-optimize at the expense of authenticity
