# Cookiecutter Template for Python Packages


What are the ingredients of this template?

- local testing/linting: pre-commit and tox
  - testing: pytest, coverage
  - linting: flake8, pylint?
  - configuration: setup.cfg
- local packaging/docs release: Makefile
  - docs: sphinx
  - releasing: PyPI, twine, wheel

Ensure that pull requests contain valid code:
- remote testing: github actions workflow
- remote package/docs release: github actions workflow

collaboration:
- editorconfig: configs across IDE's
- contributing.md: tutorial for contributors

---

Big parts of this cookiecutter are based on
- [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
- [template-python](https://github.com/jacebrowning/template-python)
