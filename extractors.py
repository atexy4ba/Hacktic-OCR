import google.generativeai as genai
import fitz  # PyMuPDF pour extraire le texte des PDF
import json
from config import GEMINI_API_KEY

# Configuration de l'API Gemini
genai.configure(api_key=GEMINI_API_KEY)

def extract_text_from_pdf(pdf_path):
    """Extrait le texte d'un fichier PDF."""
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])
    return text

def extract_info_from_cv(cv_text):
    """Envoie le texte du CV à Gemini et récupère les infos sous forme de JSON."""
    prompt = f"""
    Tu es un expert en extraction d'informations depuis un CV.
    Analyse ce CV et retourne UNIQUEMENT un JSON contenant :
    {{
      "nom": "Nom complet du candidat",
      "ecole": "École ou université fréquentée",
      "domaine": "Domaine d'apprentissage"
    }}

    CV :
    \"\"\"{cv_text}\"\"\"

    Réponds uniquement avec un JSON valide, sans texte supplémentaire, sans explication, sans guillemets autour du JSON.
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    # Nettoyage de la réponse pour s'assurer que c'est bien du JSON
    json_text = response.text.strip("```json").strip("```").strip()

    try:
        extracted_info = json.loads(json_text)
    except json.JSONDecodeError:
        extracted_info = {"error": "Réponse non valide, vérifie le format JSON"}

    return extracted_info
