#!/usr/bin/env python3
"""
Resume Formatter - Creates perfectly formatted DOCX from JSON data
No AI calls - just pure formatting with python-docx
"""

import sys
import json
from pathlib import Path

try:
    from docx import Document
    from docx.shared import Pt, Inches
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
except ImportError:
    print("❌ ERROR: python-docx not installed")
    print("Install with: pip install python-docx --break-system-packages")
    sys.exit(1)

def create_resume_docx(data, output_path):
    """Generate perfectly formatted DOCX from JSON data"""
    
    doc = Document()
    
    # Set margins (0.5 inches)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.5)
        section.bottom_margin = Inches(0.5)
        section.left_margin = Inches(0.5)
        section.right_margin = Inches(0.5)
    
    # HEADER - Name and Contact Info (2 lines, 11pt, centered)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)

    # Build header: NAME | Title (optional clearance/credential)
    name = data.get("name", "YOUR NAME")
    title = data.get("title", "")
    clearance = data.get("clearance", "")

    header_parts = [name]
    if title:
        header_parts.append(title)
    if clearance:
        header_parts.append(f"({clearance})")

    run = p.add_run(" | ".join(header_parts))
    run.bold = True
    run.font.size = Pt(11)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(12)
    contact_info = data.get("contact", {})
    run = p.add_run(f"{contact_info.get('location', '')} | {contact_info.get('phone', '')} | {contact_info.get('email', '')}")
    run.font.size = Pt(11)

    # PROFESSIONAL SUMMARY (if provided)
    if data.get("summary"):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_after = Pt(12)
        run = p.add_run(data["summary"])
        run.font.size = Pt(10.5)

    # TECHNICAL SKILLS
    p = doc.add_paragraph()
    run = p.add_run("TECHNICAL SKILLS")
    run.bold = True
    run.underline = True
    run.font.size = Pt(10.5)
    p.paragraph_format.space_after = Pt(8)

    for category, skills in data.get("skills", {}).items():
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.left_indent = Inches(0.25)
        p.paragraph_format.space_after = Pt(4)

        run = p.add_run(f"{category}: ")
        run.bold = True
        run.font.size = Pt(10.5)

        run = p.add_run(", ".join(skills))
        run.font.size = Pt(10.5)
    
    # PROFESSIONAL EXPERIENCE
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("PROFESSIONAL EXPERIENCE")
    run.bold = True
    run.underline = True
    run.font.size = Pt(10.5)

    for exp in data.get("experiences", []):
        # Company and title with right-aligned dates
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)

        # Right tab stop at 7.5 inches for dates
        tab_stops = p.paragraph_format.tab_stops
        tab_stops.add_tab_stop(Inches(7.5), WD_TAB_ALIGNMENT.RIGHT)

        run = p.add_run(f"{exp['company']} | {exp['title']}")
        run.bold = True
        run.font.size = Pt(10.5)

        run = p.add_run("\t")

        run = p.add_run(exp['dates'])
        run.font.size = Pt(10.5)

        # Bullets
        for bullet in exp['bullets']:
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.left_indent = Inches(0.25)
            p.paragraph_format.space_after = Pt(4)

            run = p.add_run(f"{bullet['title']}: ")
            run.bold = True
            run.font.size = Pt(10.5)

            run = p.add_run(bullet['text'])
            run.font.size = Pt(10.5)
    
    # EDUCATION & CERTIFICATES
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    run = p.add_run("EDUCATION & CERTIFICATES")
    run.bold = True
    run.underline = True
    run.font.size = Pt(10.5)

    for edu in data.get("education", []):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.left_indent = Inches(0.25)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(edu)
        run.font.size = Pt(10.5)
    
    # Save
    doc.save(output_path)
    print(f"✅ Resume saved to: {output_path}")

def main():
    if len(sys.argv) < 3:
        print("""
Resume Formatter
================

Usage:
  python3 create_resume.py <data.json> <output.docx>

Example:
  python3 create_resume.py resume_data.json my_resume.docx

This script takes JSON data (from Claude) and creates a perfectly formatted DOCX.
""")
        sys.exit(0)
    
    json_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not Path(json_file).exists():
        print(f"❌ Error: JSON file not found: {json_file}")
        sys.exit(1)
    
    print(f"📄 Reading data from: {json_file}")
    
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON file: {e}")
        sys.exit(1)
    
    print(f"📝 Creating resume: {output_file}")
    
    create_resume_docx(data, output_file)
    
    print("✅ Done!")

if __name__ == "__main__":
    main()
