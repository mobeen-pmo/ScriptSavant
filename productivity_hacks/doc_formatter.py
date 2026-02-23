import os
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def format_document():
    print("\n" + "="*40)
    print("   SCRIPT SAVANT: DOCUMENT FORMATTER")
    print("="*40)

    file_path = input("\n📄 Enter the path of the DOCX file to format: ").strip('"')
    
    if not os.path.exists(file_path) or not file_path.endswith('.docx'):
        print("❌ Error: Valid DOCX file not found! Make sure it is a Word document.")
        return

    try:
        doc = Document(file_path)
        print("\n🔄 Applying formal structuring... please wait.")

        # 1. Update the baseline 'Normal' style for the whole document
        style = doc.styles['Normal']
        font = style.font
        font.name = 'Times New Roman'
        font.size = Pt(12)
        
        # 2. Iterate through every paragraph to apply specific rules
        for para in doc.paragraphs:
            # Format standard text paragraphs
            if para.style.name == 'Normal':
                para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                para.paragraph_format.line_spacing = 1.5
                para.paragraph_format.space_after = Pt(12)  # Add space between paragraphs
            
            # Format Headings (Make them bold, Arial, and left-aligned)
            elif para.style.name.startswith('Heading'):
                para.alignment = WD_ALIGN_PARAGRAPH.LEFT
                para.paragraph_format.space_after = Pt(6)
                for run in para.runs:
                    run.font.name = 'Arial'
                    run.font.bold = True

        # 3. Save the new beautified document
        output_path = file_path.replace(".docx", "_formatted.docx")
        doc.save(output_path)
        
        print(f"\n✅ SUCCESS! Formatted document saved as: {output_path}")

    except Exception as e:
        print(f"\n❌ ERROR: {e}")

if __name__ == "__main__":
    format_document()
