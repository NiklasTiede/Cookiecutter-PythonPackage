# Cookiecutter Template for Python Packages

What are the ingredients of this template?

Local testing/linting is controlled by pre-commit and a Makefile
- testing: pytest, coverage (tox)
- linting: flake8

Local release (package/docs) is controlled by a Makefile
- docs: sphinx, readthedocs
- release: PyPI, twine, wheel

Remote tests to ensure that pullrequests contain good code:
- CI (testing): github actions workflow
- CD (pypi release): github actions workflow

Collaboration standards:
- editorconfig: configs across IDE's
- contributing.md: tutorial for contributors

---

Big parts of this cookiecutter are based on:
- [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
- [template-python](https://github.com/jacebrowning/template-python)
