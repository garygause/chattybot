# BOOTSTRAP

Actions taken to initialize the project.

```bash
pyenv local 3.11.10
poetry init
```

Edit the generated pyproject.toml, add dependencies (see pyproject.toml).

```bash
mkdir <project-name>
touch <project-name>/__init__.py
poetry install
poetry env activate
```
