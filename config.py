import google.generativeai as genai
import json

# Remplace avec ta clé API Google Gemini
GEMINI_API_KEY = "AIzaSyCpNeraYEWUfiUW4M9jGLn47l9WeKmN7mc"

# Configuration de l'API
genai.configure(api_key=GEMINI_API_KEY)

def extract_info_from_cv(cv_text):
    prompt = f"""
    Tu es un expert en extraction d'informations depuis un CV.  
    Analyse ce CV et retourne uniquement les informations suivantes en format JSON :
    - Le nom du candidat
    - L'école ou université fréquentée
    - Le domaine d'apprentissage

    CV :
    \"\"\"{cv_text}\"\"\"

    Réponds uniquement avec un JSON valide, sans texte supplémentaire.
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    # Extraire et parser la réponse en JSON
    try:
        extracted_info = json.loads(response.text)
    except json.JSONDecodeError:
        extracted_info = {"error": "Réponse non valide, vérifie le format JSON"}

    return extracted_info

# Exemple d'utilisation avec un CV en texte brut
cv_text = """
Jean Dupont
Étudiant en Master Informatique à l'Université de Paris
Compétences : Python, Machine Learning, Bases de données
"""

result = extract_info_from_cv(cv_text)
print(result)
