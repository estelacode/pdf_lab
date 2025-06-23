# PDF Lab

## Objective
Create an app to extract text from PDFs. It uses libraries to perform the text extraction such as pymupdf, llama-parse, etc.

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
git remote add origin https://github.com/estelacode/pdf_lab.git
git remote -v  # Verify the remote repository is added
```

☑️ Step 6: Add first commit and push the current branch and set the remote as upstream
```bash
git add README.md
git commit -m "README.md"
git push --set-upstream origin master 
git push -u origin master
```

☑️ Step 7:  Add and remove dependencies
```bash
uv add [OPTIONS] <PACKAGES>...  # Add dependencies to the project
uv remove [OPTIONS] <PACKAGES>... # Remove dependencies from the project.
```

## Usage
```bash
cd pdf_lab
uv run main.py
```

## Build the artifact
```bash
uv build
```
## Requirements
```bash
uv pip freeze > requirements.txt
```

## Developer mode
```bash
uv pip install -e . #
uv pip install --editable . # Install the editable package based on the provided local file path.
```

## Docker Image
1. Create a docker image
```bash
docker build -t pdf_lab . # build your Docker image
```
2. Create a docker container
```bash
docker run -d -p 7860:7860 pdf_lab
```
3. Create a docker container with enviroment variables
```bash
docker run -d -p 7860:7860 -e LLAMA_CLOUD_API_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXX" pdf_lab
```


## Tech Stack
* [Gradio](https://www.gradio.app/docs)
* [Rancher Desktop](https://docs.rancherdesktop.io/)
* [uv](https://docs.astral.sh/uv/concepts/projects/dependencies/)

#### PDF Procesing Libraries
* [Llama Parse](https://www.llamaindex.ai/llamaparse)
* [PyMuPDF](https://github.com/pymupdf/PyMuPDF)
* [pdfminer.six](https://pypi.org/project/pdfminer.six/)