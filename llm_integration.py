import os
from google.cloud import language_v1
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

# Set up Google Cloud credentials
credentials = service_account.Credentials.from_service_account_file('bnja-bhai-8fe37d615536.json')
language_client = language_v1.LanguageServiceClient(credentials=credentials)
translate_client = translate.Client(credentials=credentials)

def extract_entities(text):
    # Ensure text is a string
    if isinstance(text, bytes):
        text = text.decode('utf-8')  # Convert bytes to string

    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = language_client.analyze_entities(request={'document': document})
    entities = [entity.name for entity in response.entities]
    return entities

def summarize_text(text):
    sentences = text.split('.')
    summary = '.'.join(sentences[:3]) + '.'
    return summary

def classify_document(text):
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = language_client.classify_text(document=document)
    categories = [category.name for category in response.categories]
    return categories

def translate_text(text, target_language='es'):
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']
