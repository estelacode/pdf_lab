# Llama Parse Lab

## Objective
Create an app to extract text from PDFs. It uses Llama Parse library to perform the text extraction.

## Installation

☑️ Step 1: Create Virtual Enviroment
```bash
py -3.13 -m venv .venv
```

☑️ Step 2: Activate Virtual Enviroment
```bash
.venv\Script\activate
```

☑️ Step 3: Install UV
```bash
pip install uv
```

☑️ Step 4: Create a project with uv
```bash
uv init
```
☑️ Step 5: Link my local repository to my Github remote repository
```bash
git remote add origin https://github.com/estelacode/llama_parse_lab.git
git remote -v  # Verify the remote repository is added
```

☑️ Step 6: Add first commit and push the current branch and set the remote as upstream
```bash
git add README.md
git commit -m "README.md"
git push --set-upstream origin master 
git push -u origin master
```

## Project Structure

## Tech Stack
* [Gradio](https://www.gradio.app/docs)
* [Rancher Desktop](https://docs.rancherdesktop.io/)
* [Llama Parse](https://www.llamaindex.ai/llamaparse)
* [uv](https://docs.astral.sh/uv/concepts/projects/dependencies/)

* [PyMuPDF](https://github.com/pymupdf/PyMuPDF)
* [pdfminer.six](https://pypi.org/project/pdfminer.six/)