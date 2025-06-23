
import gradio as gr
from llama_parse_lab.utils import load_pdf_pymupdf, load_pdf_llama_parse

def select_method_extraction(path_file:str, method_extraction:str)->str:
    
    """
    Selects the method to extract text from a PDF file.

    Parameters:
    path_file (str): Path to the PDF file.
    method_extraction (str): The method to use for extraction, either "pymupdf" or "llama_parse".

    Returns:
    str: The extracted text from the PDF file.
    """

    if method_extraction == "pymupdf":
        return load_pdf_pymupdf(path_file)
    else:
        return load_pdf_llama_parse(path_file)
    

demo = gr.Interface(fn = select_method_extraction, 
                    inputs = [gr.File(file_types=[".pdf"]), gr.Dropdown(["pymupdf", "llama_parse"])], 
                    outputs = gr.Text())
demo.launch()
