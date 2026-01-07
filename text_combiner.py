with open("data/processed/pdf_text.txt","r",encoding="utf-8") as f:
    pdf_text = f.read()

with open("data/raw/website.txt","r",encoding="utf-8") as f:
    website_text = f.read()

combined_text = (pdf_text + "\n\n" +website_text)

with open("data/processed/combined_text.txt","w",encoding="utf-8") as f:
    f.write(combined_text)