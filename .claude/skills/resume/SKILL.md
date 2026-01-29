---
name: resume
description: Generate a tailored resume from master resume data and a job description. Use when the user asks to create, build, or generate a resume for a specific job.
argument-hint: [job-description-file] [resume-data-json]
allowed-tools: Read, Write, Edit, Bash, Glob, WebSearch
---

# Resume Builder

Build a tailored resume from structured master resume data and a job description.

**IMPLEMENTATION APPROACH:**
- **YOU (Claude Code) do ALL the AI work** - analysis, scoring, rewriting, optimization
- **Python script (create_resume.py) does ONLY formatting** - converts JSON to .docx
- **NO external API calls needed** - you're already here doing the work!

## When invoked with arguments:
- First argument: Path to job description file (e.g., backend_job.txt)
- Second argument (optional): Path to master resume JSON (defaults to resume_data_example.json)

## Steps to follow:

1. **Read input files**:
   - Read the job description to understand requirements
   - Read the master resume data JSON containing all experiences, skills, and education
   - If job file doesn't exist, create a sample one for testing

1.5. **Generate Professional Summary** (YOU create this):
   - Create a **2 sentence maximum** professional summary optimized for ATS and human readers
   - Front-load with job title and years of experience matching the posting
   - Pack with 5-7 top keywords from job description
   - Highlight 1 key achievement with metric **ONLY if it exists in master resume**
   - **STRICT LENGTH:** Max 40 words total (roughly 3 lines on resume)
   - **NO FABRICATION:** Only use metrics/achievements explicitly in master resume bullets
   - Example: "Senior Backend Engineer with 6+ years building scalable Java Spring Boot microservices and event-driven systems on AWS using Kafka, Kubernetes (K8s), and Terraform. Architected distributed systems and led engineering teams."
   - Add this to the tailored JSON as a "summary" field

2. **AI Job Analysis** (YOU do this directly):
   - Read and deeply analyze the job description
   - Extract required skills (10-20 specific technical skills)
   - Identify desired experience areas (5-10 areas)
   - Extract key responsibilities (5-7 main duties)
   - Identify ATS keywords (25-40 keywords including synonyms)
   - Extract impact words and action verbs
   - Note company culture keywords
   - Determine seniority level and role focus
   - Present analysis summary to user

3. **Score Experience Bullets** (YOU score each one):
   - For each bullet in master resume data, YOU analyze and score 0-100 based on:
     - Technical skill alignment (40 points)
     - Experience level/scope match (30 points)
     - Responsibility relevance (20 points)
     - Cultural/soft skill fit (10 points)
   - Rank all bullets by score
   - Show top scored bullets to user

4. **Select Top Bullets** (YOU decide):
   - Select highest scoring bullets per position
   - **STRICT position limits for one-page fit (with 10.5pt body font):**
     - Most recent position: 3-5 bullets max (prioritize impact, architecture, leadership)
     - Previous senior positions: 2-3 bullets each
     - Mid-level positions: 1-2 bullets each
     - Early career positions: 1 bullet or omit entirely
     - Total: 10-12 bullets maximum for one-page fit
   - **Bullet Selection Priority:**
     - For senior/lead roles: prioritize cross-organizational impact, technical strategy, architecture, team leadership
     - Look for: "company-wide", "adopted across", "established standards", "selected technologies", "architected"
     - For all levels: prioritize metrics, quantifiable impact, and job-relevant keywords
   - If resume still overflows, reduce older position bullets or eliminate earliest positions

5. **AI Bullet Rewriting** (YOU rewrite directly):
   - For each selected bullet, YOU rewrite it to match job language
   - Use job keywords naturally
   - Apply strong action verbs from job description
   - **STRICT word limits (ENFORCE THESE):**
     - Lead roles: 32 words max (~2 lines)
     - Senior roles: 28 words max (~1.75 lines)
     - Mid-level/older roles: 12 words max (~1 line)
   - **ABSOLUTELY CRITICAL - NO FABRICATION:**
     - **NEVER make up metrics, numbers, team sizes, or performance improvements**
     - **ONLY use information explicitly stated in the master resume bullet text**
     - If a metric/number is in the master resume, you can use it
     - If NO metric exists, you CANNOT add one - just rewrite with keywords
     - Example: If master says "serving hundreds of users" → you can say "serving hundreds of users"
     - Example: If master says "improved uptime" with no number → you CANNOT say "improved uptime 50%"
   - **CRITICAL:** Count words - if over limit, cut ruthlessly while keeping impact and keywords

   **CRITICAL - Leadership Language for Lead/Senior Roles:**
   - For Lead Software Engineer bullets, emphasize LEADERSHIP and SCOPE:
     - Use verbs: Architected, Led, Designed, Drove, Established, Scaled, Owned
     - Show scope: team impact, system scale, organizational influence
     - Include metrics: percentages, team size, user count, performance gains
     - Emphasize: architectural decisions, mentorship, cross-team collaboration, technical strategy
   - Make it clear you're operating at a LEAD level, not just coding

   **ATS Optimization (AI Screeners):**
   - Pack each bullet with 3-5 relevant keywords from job description
   - Use EXACT keyword matches from job posting (e.g., if job says "Java Spring Boot", use that exact phrase)
   - Include BOTH acronyms AND full forms in same bullet (e.g., "Kubernetes (K8s)", "CI/CD continuous integration")
   - Mirror job posting's exact phrases (e.g., "event-driven systems" not "event-driven architecture" if job uses former)
   - Front-load important keywords early in the bullet
   - Use industry-standard terminology
   - Skills section should match job posting's keyword order when possible
   - Ensure no required skill from job is missing from resume

   **Human Screener Optimization:**
   - **RESULTS FIRST:** Start with the outcome/impact, then explain how you achieved it
     - Bad: "Built microservices using Kafka"
     - Good: "Reduced latency 40% by building event-driven microservices with Kafka and RabbitMQ"
   - **Quantify EVERYTHING possible:**
     - Scale: "serving 10M daily users", "managing 50+ microservices", "processing 1B events/day"
     - Team: "led 5 engineers", "mentored 3 junior developers", "collaborated with 4 teams"
     - Performance: "reduced costs 30%", "improved throughput 3x", "decreased MTTR by 50%"
     - Time: "accelerated deployment from 2 hours to 15 minutes"
   - Show business value, not just technical tasks
   - Make it scannable: strong opening verb + clear achievement
   - Demonstrate progression and increasing responsibility
   - Every Lead bullet should show scope (team size OR system scale OR organizational impact)

6. **Generate Context-Aware Titles** (YOU create titles):
   - For each bullet, YOU create a 2-4 word title
   - Emphasize aspects most relevant to the target job
   - Use professional terminology from the job description

7. **Optimize Skills Section** (YOU reorder):
   - Reorder skills to prioritize job keywords
   - Keep skills matching ATS keywords at the front
   - **CRITICAL:** Include BOTH acronyms and full forms where needed:
     - "Kubernetes (K8s)" or list both separately
     - Ensure exact matches to job posting phrasing
   - Order skills within each category to match job posting's priority
   - Remove or de-emphasize skills not mentioned in job posting

8. **Check for Missing Skills** (YOU analyze gaps):
   - Identify skills in job description but not in master resume
   - Warn user about high-priority missing skills
   - Suggest updating master resume data if applicable

9. **Create Tailored JSON** (Use Write tool):
   - Write a new JSON file (e.g., `backend_tailored.json`) with:
     - **"summary":** Professional summary string (2-3 sentences, ATS-optimized)
     - **"contact":** Original contact info
     - **"skills":** Optimized skills (reordered, with exact keyword matches)
     - **"experiences":** Selected experiences with rewritten bullets and new titles
     - **"education":** Original education
   - This JSON follows the same structure as resume_data_example.json with added summary field

10. **Generate .docx Resume** (Use Bash tool):
    - Run: `python3 create_resume.py backend_tailored.json backend_resume.docx`
    - The Python script handles ONLY formatting - no AI work
    - Creates professionally formatted Word document
    - **Formatting specs:**
      - Header (centered, 11pt): Name | Title (optional clearance/credential) on line 1, Contact info on line 2
      - Body (10.5pt): All content after header
      - One-page format with proper margins
    - This formatting provides space for 10-12 bullets total

11. **Verify One-Page Fit** (CRITICAL):
    - After generating, ask user to confirm if resume fits on one page
    - If resume overflows:
      - **Option 1:** Reduce oldest position bullets or eliminate oldest position entirely
      - **Option 2:** Shorten professional summary to 1-2 sentences (25 words max)
      - **Option 3:** Trim bullet word counts by 10-20% (cut filler words ruthlessly)
      - **Option 4:** Reduce skills section items (keep only top ATS keywords)
    - Regenerate until it fits on one page

## Output:
- Generate a tailored `[jobname]_resume.docx` file
- Show summary of selected bullets with AI scores
- Report any missing critical skills

## Best practices:
- Use action verbs from job description (Led, Architected, Scaled, Optimized)
- Mirror language and terminology from the job posting
- Prioritize most relevant experiences
- Keep bullets dense and concise
- Maintain ATS-friendly formatting

## Writing Style by Seniority Level:

**Lead/Principal Engineer bullets should show:**
- System architecture and design decisions ("Architected", "Designed", "Established")
- Team/organizational impact ("Led 5 engineers", "Drove adoption across 3 teams")
- Strategic thinking ("Established standards", "Defined architecture patterns")
- Mentorship and influence ("Mentored", "Guided", "Championed")
- Large scope ("microservices platform serving 10M users", "cross-team initiative")
- Business outcomes ("reduced costs 40%", "accelerated delivery 3x")

**FORMULA for Lead bullets: [IMPACT METRIC] + [ACTION VERB] + [TECHNICAL DETAILS] + [SCOPE/SCALE]**
- Example: "Reduced deployment time 80% by architecting Terraform CI/CD pipelines for 30+ microservices across AWS Lambda and ECS; led 4-engineer DevOps initiative."
- Example: "Improved system throughput 3x designing Kafka event-driven architecture processing 5M events/day; established patterns adopted by 6 engineering teams."

**Senior Engineer bullets should show:**
- Technical ownership ("Built", "Implemented", "Developed")
- Some leadership ("Collaborated", "Contributed to")
- Solid technical depth ("Spring Boot microservices with Kafka event streaming")
- Quality focus ("TDD", "comprehensive tests", "99.9% uptime")

**Mid-level bullets should show:**
- Execution and implementation
- Technical growth
- Team collaboration

**Key difference:** Lead = "I designed the system and led the team" vs Senior = "I built key features and contributed to architecture"
