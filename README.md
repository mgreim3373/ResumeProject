# AI-Powered Resume Builder

Generate ATS-optimized, tailored resumes from your master resume data using Claude Code.

## Overview

This resume builder uses Claude AI to analyze job descriptions and automatically generate tailored resumes optimized for both ATS (Applicant Tracking Systems) and human recruiters.

**Key Features:**
- Scores and selects most relevant experience bullets for each job
- Rewrites bullets with job-specific keywords while maintaining truthfulness
- Generates optimized professional summaries
- Reorders skills to match job requirements
- Produces one-page, professionally formatted Word documents

## How It Works

1. **You maintain a master resume** (`resume_data_example.json`) with ALL your experiences, skills, and achievements
2. **You provide a job description** (text file)
3. **Claude analyzes the job** and scores each bullet for relevance
4. **Claude generates a tailored resume** optimized for that specific role
5. **Python formats it perfectly** into a `.docx` file

## Setup

### 1. Install Dependencies

```bash
pip install python-docx --break-system-packages
```

### 2. Create Your Master Resume Data

Copy `resume_data_example.json` and customize it with your information:

```json
{
  "name": "YOUR NAME",
  "title": "Your Job Title",
  "clearance": "Optional Clearance/Credential",
  "contact": {
    "location": "City, State",
    "phone": "555.123.4567",
    "email": "your.email@example.com"
  },
  "skills": {
    "Category 1": ["Skill1", "Skill2", "Skill3"],
    "Category 2": ["Skill4", "Skill5"]
  },
  "experiences": [
    {
      "company": "COMPANY NAME",
      "title": "Your Title",
      "dates": "MM/YYYY -- MM/YYYY",
      "bullets": [
        {
          "title": "Short Title",
          "text": "Full description of what you did and the impact.",
          "keywords": ["keyword1", "keyword2"],
          "categories": ["Category"]
        }
      ]
    }
  ],
  "education": [
    "Degree, University (Year)",
    "Certification Name (Year)"
  ]
}
```

**Important Tips for Master Resume Data:**

- **Be truthful:** Only include actual accomplishments with real metrics
- **Be comprehensive:** Include ALL experiences - the AI will select the best ones
- **Include metrics:** Whenever possible, quantify impact (users served, % improvement, team size, etc.)
- **Add keywords:** Help the AI understand what technologies and concepts each bullet demonstrates
- **Title field (optional):** Your current/target title (e.g., "Senior Software Engineer")
- **Clearance field (optional):** Any clearance or credential to display (e.g., "Active Secret Clearance", "PMP Certified")

### 3. Install the Claude Code Skill

The `/resume` skill is located in `.claude/skills/resume/skill.md`. Claude Code automatically loads skills from this directory.

## Usage

### Generate a Tailored Resume

**Option 1: Use sample data (for testing)**
```bash
/resume sample_job.txt
```
This will use `resume_data_example.json` by default.

**Option 2: Use your own master resume**
```bash
/resume sample_job.txt my_resume_data.json
```

**Option 3: For a real job application**
1. Save the job description to a text file (e.g., `fintech_job.txt`)
2. Run the resume skill:
   ```bash
   /resume fintech_job.txt my_resume_data.json
   ```

**Try the included samples:**
```bash
# Full-stack job example
/resume sample_job.txt my_resume_data.json

# Backend job example
/resume backend_job.txt my_resume_data.json
```

### What Happens

Claude will:
1. Analyze the job description for required skills, keywords, and responsibilities
2. Score every bullet in your master resume (0-100) based on relevance
3. Select the top bullets for a one-page resume (typically 10-12 bullets)
4. Rewrite bullets with job-specific keywords while staying truthful
5. Generate an optimized professional summary (40 words max)
6. Reorder skills to match job requirements
7. Create `[jobname]_tailored.json` with the optimized data
8. Generate `[jobname]_resume.docx` with perfect formatting

### Customizing Bullet Limits

By default, the skill uses these limits for one-page fit:
- Most recent position: 3-5 bullets
- Previous senior positions: 2-3 bullets each
- Mid-level positions: 1-2 bullets each
- Early career: 1 bullet or omit

**To customize for your career stage and resume length:**

Edit `.claude/skills/resume/skill.md` and modify the bullet limits in **Step 4** to match your situation.

Examples:
- **Senior with 15+ years:** May need tighter limits (3/2/1/0) to fit one page
- **Mid-level with 5 years:** Can use default limits (3-5/2-3/1-2)
- **Entry-level:** May allocate more bullets to recent positions

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install python-docx --break-system-packages
   ```

2. **Copy and customize your master resume:**
   ```bash
   cp resume_data_example.json my_resume_data.json
   # Edit my_resume_data.json with your actual experience
   ```

3. **Test with sample job:**
   ```bash
   /resume sample_job.txt my_resume_data.json
   ```

4. **Check the generated resume:**
   - `sample_tailored.json` - Tailored resume data
   - `sample_resume.docx` - Formatted Word document

## File Structure

```
project/
├── README.md                          # This file
├── .gitignore                         # Excludes generated files from git
├── resume_data_example.json           # Sample master resume data (use as template)
├── create_resume.py                   # Python formatter (formatting only)
├── .claude/skills/resume/skill.md     # Claude Code skill definition
├── sample_job.txt                     # Example full-stack job description
├── backend_job.txt                    # Example backend job description
└── (generated files)
    ├── *_tailored.json                # Generated tailored resume data
    └── *_resume.docx                  # Generated Word documents
```

## Key Principles

### 1. No Fabrication
The AI **never** makes up metrics, team sizes, or accomplishments. It only uses information explicitly in your master resume data.

### 2. ATS Optimization
- Uses exact keyword matches from job descriptions
- Includes both acronyms and full forms (e.g., "Kubernetes (K8s)")
- Front-loads important keywords in bullets
- Mirrors job posting language

### 3. Human Optimization
- Starts bullets with impact/outcome
- Quantifies everything possible
- Shows business value, not just technical tasks
- Demonstrates progression and responsibility

### 4. One-Page Focus
- Uses strict word limits per bullet (Lead: 32 words, Senior: 28 words, Mid-level: 12 words)
- Prioritizes most recent and relevant experience
- Omits or condenses early career positions

## Tips for Best Results

### Writing Master Resume Bullets

**Good bullet (specific, quantified, impactful):**
```
"Led architecture and development of customer engagement platform serving 500k daily users using React, TypeScript, and Node.js microservices on AWS; mentored team of 3 engineers and established code review standards."
```

**Bad bullet (vague, no metrics):**
```
"Worked on platform features and helped team members."
```

### Professional Summary

The AI generates a 2-sentence summary (40 words max) optimized for ATS. It:
- Front-loads with your title and years of experience
- Packs in 5-7 top keywords from the job
- Highlights 1 key achievement (only if in your master resume)

Example:
```
"Senior Backend Engineer with 6+ years building scalable Java Spring Boot microservices and event-driven systems on AWS using Kafka, Kubernetes, and Terraform. Architected distributed systems serving millions of users."
```

### Job Description Files

- Save as plain text (.txt)
- Include the full job posting (requirements, responsibilities, nice-to-haves)
- More detail = better keyword matching

## Troubleshooting

### Resume Overflows One Page

If the generated resume is too long:
1. Claude will suggest reducing oldest position bullets
2. You can edit `.claude/skills/resume/skill.md` to use tighter bullet limits
3. Shorten professional summary to 1-2 sentences (25 words)
4. Remove skills not mentioned in job posting

### Missing Required Skills

If the job requires skills you don't have in your master resume:
1. Claude will warn you about missing skills
2. If you DO have the skill but forgot to add it, update `resume_data.json`
3. If you DON'T have the skill, consider whether you still want to apply

### Python Errors

If you get "python-docx not installed":
```bash
pip install python-docx --break-system-packages
```

## Example Workflow

1. **Maintain your master resume:**
   - Add new accomplishments monthly
   - Quantify impact whenever possible
   - Keep ALL experiences (AI selects the best)

2. **Find a job to apply for:**
   - Save job description to `fintech_job.txt`

3. **Generate tailored resume:**
   ```bash
   /resume fintech_job.txt my_resume_data.json
   ```

4. **Review output:**
   - Check `fintech_tailored.json` for selected bullets
   - Open `fintech_resume.docx` to verify formatting
   - Ensure one-page fit

5. **Apply with confidence:**
   - Resume is ATS-optimized with exact keywords
   - Human-readable with metrics and impact
   - Tailored specifically for this role

## Advanced: Customizing Formatting

The Python script (`create_resume.py`) handles all formatting. To customize:

- **Fonts:** Edit `Pt(11)` and `Pt(10.5)` values
- **Margins:** Edit `Inches(0.5)` values
- **Spacing:** Edit `Pt(2)`, `Pt(4)`, `Pt(8)`, `Pt(12)` values
- **Layout:** Modify paragraph styles and alignment

The script is deliberately simple (no AI calls) so you can easily customize formatting without affecting the AI logic.

## License

Free to use and modify for personal use.

## Credits

Built using Claude Code and the Claude API.
