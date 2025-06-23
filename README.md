# Llama Parse Lab

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