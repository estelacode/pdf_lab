import pymupdf
from llama_cloud_services import LlamaParse
import os
from dotenv import load_dotenv

load_dotenv()


def load_pdf_pymupdf(pdf_file:str)->str:
    
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



def load_pdf_llama_parse(pdf_file:str)->str:
    
    """
    This function extracts text from a PDF file using the LlamaParse service.

    Parameters:
    pdf_file (str): Path to the PDF file.

    Returns:
    str: The extracted text from the PDF file.

    Raises:
    ValueError: If the LLAMA_CLOUD_API_KEY environment variable is not set.

    Note:
    - The function requires a valid API key for the LlamaParse service to be set 
      in the LLAMA_CLOUD_API_KEY environment variable.
    - The text from the PDF is returned as a single document.
    """
    
     # Check if the environment variable is set
    if not os.getenv("LLAMA_CLOUD_API_KEY"):
        raise ValueError("LLAMA_CLOUD_API_KEY is not set")
    api_key = os.getenv("LLAMA_CLOUD_API_KEY")
    
    # Create an instance of the LlamaParse class
    parser = LlamaParse(api_key=api_key, num_workers=1,verbose=True,language="en")

    # Parse the PDF file
    job_result = parser.parse(pdf_file)

    # Get the text from the job result in a single document
    text_documents = job_result.get_text_documents(split_by_page=False)

    # Get the text from the first document
    text = text_documents[0].text

    return text


  