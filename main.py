import os
import json
from extractors import extract_text_from_pdf, extract_info_from_cv

DATA_DIR = "data"
OUTPUT_DIR = "output"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def process_pdfs():
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(DATA_DIR, filename)
            print(f"\n📄 Traitement du fichier : {filename}...\n")

            # 1️⃣ Extraction du texte via OCR
            extracted_text = extract_text_from_pdf(pdf_path)
            print("🔍 Texte détecté par l'OCR :\n")
            print(extracted_text)  # 🔴 Affichage du texte OCR

            # 2️⃣ Extraction des infos depuis l'IA
            extracted_info = extract_info_from_cv(extracted_text)
            
            # 3️⃣ Sauvegarde en JSON
            output_path = os.path.join(OUTPUT_DIR, filename + ".json")
            with open(output_path, "w", encoding="utf-8") as json_file:
                json.dump(extracted_info, json_file, indent=4, ensure_ascii=False)

            print(f"\n✅ Résultat sauvegardé dans : {output_path}")

if __name__ == "__main__":
    process_pdfs()
