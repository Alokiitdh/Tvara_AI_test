from pypdf import PdfReader

# This function will extract some sentence from the pdf

def extract_sentences_from_pdf(pdf_path, max_sentences=5):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + " "

    # very rough split into sentences
    raw_sentences = text.split(".")
    sentences = [s.strip() for s in raw_sentences if s.strip()]
    return sentences[:max_sentences]

PDF_PATH = "task_c\Artificial Intelligence and Its Future Technologies.pdf"
pdf_sentences = extract_sentences_from_pdf(PDF_PATH)
print("Sentences from PDF:")
for s in pdf_sentences:
    print("-", s)
