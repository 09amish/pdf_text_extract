import tkinter as tk
from tkinter import filedialog, Text, messagebox
from pdf_to_text import pdf_to_text
from ocr_integration import extract_images_from_pdf, ocr_images
from text_preprocessing import preprocess_text
from llm_integration import extract_entities, summarize_text, classify_document, translate_text

class DocumentProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Document Processor")
        
        self.upload_button = tk.Button(root, text="Upload PDF", padx=10, pady=5, fg="white", bg="#263D42", command=self.upload_pdf)
        self.upload_button.pack()
        
        self.text_display = Text(root, height=20, width=100)
        self.text_display.pack()
        
        self.process_button = tk.Button(root, text="Process Document", padx=10, pady=5, fg="white", bg="#263D42", command=self.process_document)
        self.process_button.pack()

    def upload_pdf(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.file_path:
            messagebox.showinfo("File Selected", f"Selected file: {self.file_path}")
        
    def process_document(self):
        if not hasattr(self, 'file_path'):
            messagebox.showerror("Error", "Please upload a PDF file first")
            return
        
        # Convert PDF to text
        text = pdf_to_text(self.file_path)
        images = extract_images_from_pdf(self.file_path)
        ocr_text = ocr_images(images)
        
        full_text = text + "\n" + ocr_text
        
        # Preprocess text
        sentences, tokens = preprocess_text(full_text)
        
        # Display preprocessed text
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, "Processed Text:\n")
        self.text_display.insert(tk.END, "\n".join(sentences))
        
        # Extract entities
        entities = extract_entities(full_text)
        summary = summarize_text(full_text)
        classification = classify_document(full_text)
        translation = translate_text(full_text, "Spanish")
        
        # Display LLM results
        self.text_display.insert(tk.END, "\n\nEntities:\n" + entities)
        self.text_display.insert(tk.END, "\n\nSummary:\n" + summary)
        self.text_display.insert(tk.END, "\n\nClassification:\n" + classification)
        self.text_display.insert(tk.END, "\n\nTranslation (Spanish):\n" + translation)

if __name__ == "__main__":
    root = tk.Tk()
    app = DocumentProcessorApp(root)
    root.mainloop()
