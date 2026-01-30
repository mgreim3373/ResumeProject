# AI-Powered Resume Builder

Generate ATS-optimized, tailored resumes from your master resume data using Claude Code.

## Overview

This resume builder uses Claude AI to analyze job descriptions and generate tailored resumes optimized for Applicant Tracking Systems (ATS). It preserves your original writing while making surgical keyword insertions to maximize match rates.

**Key Features:**
- Preserves your original resume text with minimal changes
- Asks about skill gaps before making assumptions
- Presents ATS optimization suggestions one-by-one for your approval
- Interactive screenshot feedback to ensure one-page fit
- Generates professionally formatted Word documents

## How It Works

1. **You maintain a master resume** (`master_resume.json`) with ALL your experiences and skills
2. **You provide a job description** (text file)
3. **Claude identifies gaps** and asks if you have experience with missing skills
4. **Claude generates a tailored summary** optimized for the job
5. **Claude reorders skills** to prioritize job keywords
6. **ATS optimization loop** presents keyword insertion opportunities one-by-one
7. **Screenshot verification** ensures the resume fits on one page
8. **Python formats it** into a `.docx` file

## Setup

### 1. Install Dependencies

```bash
pip install python-docx --break-system-packages
```

### 2. Create Your Master Resume Data

Edit `master_resume.json` with your information:

```json
{
  "name": "YOUR NAME",
  "title": "Your Job Title (Optional Credential)",
  "contact": {
    "location": "City, State",
    "phone": "555.123.4567",
    "email": "your.email@example.com"
  },
  "summary": "Your default professional summary (will be rewritten for each job).",
  "skills": {
    "Category 1": ["Skill1", "Skill2", "Skill3"],
    "Category 2": ["Skill4", "Skill5"]
  },
  "experiences": [
    {
      "company": "COMPANY NAME",
      "title": "Your Current Title",
      "dates": "MM/YYYY - Present",
      "previousTitle": "Previous Title (optional - for promotions)",
      "previousDates": "MM/YYYY - MM/YYYY (optional)",
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

**Field Notes:**
- `title`: Include clearance or credentials here (e.g., "Senior Engineer (Active Secret Clearance)")
- `previousTitle` / `previousDates`: Optional - use for showing promotions at same company
- `keywords` / `categories` in bullets: Optional - help Claude understand what each bullet demonstrates
- Any number of experiences and bullets supported
- Education can be strings or objects

## Usage

### Generate a Tailored Resume

```bash
/resume job_description.txt
```

Or specify a custom master resume:
```bash
/resume job_description.txt my_resume_data.json
```

### What Happens

1. **Gap Analysis**: Claude identifies skills in the job posting that aren't in your resume
2. **Gap Questions**: You're asked about missing skills, where you used them, and Claude suggests which bullet to add them to
3. **Resume Generation**: Creates tailored JSON with new summary and reordered skills
4. **ATS Optimization Loop**:
   - Presents keyword insertion opportunities one-by-one
   - You approve or skip each change
   - All approved changes are applied at once
   - ATS score calculated once at the end
5. **Screenshot Verification**: You share a screenshot if it overflows one page
6. **Final Report**: Shows matched keywords and remaining gaps
7. **Cleanup**: Deletes intermediate `*_tailored.json` files

### Example Session

```
> /resume backend_job.txt

Gap Analysis:
- GraphQL: Not in resume
- SonarQube: Not in resume

Q: Do you have GraphQL experience?
A: No

Q: Do you have SonarQube experience?
A: Yes, at RAFT for code quality checks

Claude: I'll add SonarQube to your RAFT Cloud & Analytics bullet.

[Resume generated with new summary and reordered skills]

Q: Add 'frontend development' to summary?
   Current: "...Expert in React, TypeScript, microservices..."
   Proposed: "...Expert in React, TypeScript, frontend development, microservices..."
A: Yes

Q: Add 'CI/CD' to GitLab CI mention?
   Current: "...implementing GitLab CI pipelines..."
   Proposed: "...implementing GitLab CI/CD pipelines..."
A: Yes

[...more suggestions...]

All changes applied.

Final ATS Score: 95% (21/22 keywords)

Please check if resume fits on one page. Share screenshot if overflow.

[User confirms it fits]

Resume Complete!
- Matched Keywords: 21/22 (95%)
- File: backend_resume.docx
```

## File Structure

```
project/
├── README.md                          # This file
├── master_resume.json                 # Your master resume data
├── create_resume.py                   # Python formatter (formatting only)
├── .claude/skills/resume/skill.md     # Claude Code skill definition
├── example_job.txt                    # Example job description
└── (generated files)
    └── *_resume.docx                  # Generated Word documents
```

## Key Principles

### 1. Preserve Original Text
Your bullet text is preserved as much as possible. Only surgical keyword insertions are made (e.g., adding "high-performance" or "system integration").

### 2. No Fabrication
Claude **never** makes up skills or experience. If you don't have a skill, it remains a gap.

### 3. User Approval
Every text change is presented for your approval before being applied.

### 4. ATS Optimization
- Uses exact keyword matches from job descriptions
- Reorders skills to prioritize job requirements
- Includes both acronyms and full forms (e.g., "Kubernetes (K8s)")

### 5. One-Page Focus
The screenshot feedback loop helps trim content to fit one page while preserving ATS keywords.

## Customizing Formatting

The Python script (`create_resume.py`) handles all formatting. To customize:

- **Fonts**: Edit `FONT_HEADER` and `FONT_BODY` constants
- **Sizes**: Edit `SIZE_NAME`, `SIZE_BODY`, `SIZE_SECTION` values
- **Margins**: Edit `MARGINS` value (in inches)
- **Spacing**: Edit `SPACE_*` values (in points)

## Troubleshooting

### Resume Overflows One Page

Share a screenshot and Claude will suggest:
1. Trimming orphaned words (short lines)
2. Removing non-essential skills (not in job posting)
3. Shortening older position bullets
4. As last resort, removing oldest positions

### Missing python-docx

```bash
pip install python-docx --break-system-packages
```

### ATS Score Won't Reach 90%

If the job requires skills you don't have (like GraphQL), the score may not reach 90%. This is expected - don't fabricate experience.

## License

Free to use and modify for personal use.

## Credits

Built using Claude Code.
