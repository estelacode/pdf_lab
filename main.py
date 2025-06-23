
import gradio as gr
import pymupdf

def load_pdf(pdf_file:str)->str:
    
    """
    This function takes a PDF file and extracts all its text.
    
    Parameters:
    pdf_file (str): Path to the PDF file.
    
    Returns:
    str: The extracted text.
    """
    print(pdf_file)
    doc = pymupdf.open(pdf_file)

    text = ""
    for page in doc:
        text += str(page.get_text())
        print(f"Page {page.number}: {page.get_text().encode('utf-8')}") 
    return text


demo = gr.Interface(fn = load_pdf, inputs = gr.File(file_types=[".pdf"]), outputs = gr.Text())
demo.launch()
