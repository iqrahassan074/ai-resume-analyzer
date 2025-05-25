import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_sections(text):
    sections = {
        "Education": "",
        "Experience": "",
        "Skills": ""
    }
    lines = text.split('\n')
    current_section = None
    for line in lines:
        lower = line.lower()
        if "education" in lower:
            current_section = "Education"
        elif "experience" in lower:
            current_section = "Experience"
        elif "skills" in lower:
            current_section = "Skills"
        if current_section:
            sections[current_section] += line + "\n"
    return sections
