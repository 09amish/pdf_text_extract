import streamlit as st
from document_conversion import convert_pdf_to_text
from ocr_integration import extract_text_from_images
from text_preprocessing import preprocess_text
from llm_integration import extract_entities, summarize_text, classify_document, translate_text

def main():
    st.title("Document Processing and NLP with Google Cloud")

    uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")
    if uploaded_file is not None:
        # Pass the bytes directly to the conversion function
        text = convert_pdf_to_text(uploaded_file.getvalue())
        text += extract_text_from_images(uploaded_file.getvalue())
        preprocessed_text = preprocess_text(text)
        
        st.subheader("Extracted Text")
        st.write(preprocessed_text)
        
        entities = extract_entities(preprocessed_text)
        st.subheader("Extracted Entities")
        st.write(entities)
        
        summary = summarize_text(preprocessed_text)
        st.subheader("Summary")
        st.write(summary)
        
        categories = classify_document(preprocessed_text)
        st.subheader("Document Categories")
        st.write(categories)
        
        translation = translate_text(preprocessed_text)
        st.subheader("Translation (to Spanish)")
        st.write(translation)

if __name__ == "__main__":
    main()
