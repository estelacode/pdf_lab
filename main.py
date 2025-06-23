
import gradio as gr
from llama_parse_lab.utils import load_pdf_pymupdf, load_pdf_llama_parse



demo = gr.Interface(fn = load_pdf_llama_parse, inputs = gr.File(file_types=[".pdf"]), outputs = gr.Text())
demo.launch()
