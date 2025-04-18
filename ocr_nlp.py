import pytesseract
from PIL import Image
from langdetect import detect
from nltk.tokenize import word_tokenize
import nltk

# Download punkt tokenizer (if not already)
nltk.download('punkt_tab')

# Set Tesseract executable path (adjust if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image_path):
    # OCR for Gujarati text
    text = pytesseract.image_to_string(Image.open(image_path), lang='guj')
    return text.strip()

def normalize_text(text):
    # Simple normalization — stripping extra spaces
    return ' '.join(text.split())

def tokenize_text(text):
    # Tokenize — using English punkt tokenizer (works for Gujarati spacing too)
    tokens = word_tokenize(text, language='english')
    return tokens

def detect_language(text):
    return detect(text)

def nlp_pipeline(image_path):
    extracted_text = extract_text(image_path)
    normalized = normalize_text(extracted_text)
    tokens = tokenize_text(normalized)
    lang = detect_language(normalized)

    result = {
        'extracted_text': extracted_text,
        'normalized_text': normalized,
        'detected_language': lang,
        'tokens': tokens
    }
    return result
