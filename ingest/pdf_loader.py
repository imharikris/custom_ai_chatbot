import pdfplumber

max_pages = 25

def load_pdf(path: str)-> str:
    pages = []
    with pdfplumber.open(path) as pdf:
        pages_to_read = min(len(pdf.pages), max_pages)
        for i in range(pages_to_read):
            page= pdf.pages[i] 
            text = page.extract_text()
            if text:
                cleaned_text = ' '.join(text.split())
                pages.append(cleaned_text)
    return '\n'.join(pages)

if __name__ == "__main__":
    text = load_pdf("data/raw/document.pdf")

    with open("data/processed/pdf_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("PDF text extracted (limited to first 25 pages) and saved to data/processed/pdf_text.txt")
