<p align="center">
  <img  alt="covid19pyclient" align="center" width="500" src="docs/cookie2.jpg" />
   <h1 align="center">Cookiecutter Template for Python Packages</h1>
<p>

What makes this template different than other PyPackage templates? All commands used for development are stored within a `Makefile`! This increases automation and new contributors will know immediately about the development workflow.

Local testing/linting is controlled by `pre-commit` and a `Makefile`
- Testing: pytest, coverage (tox)
- Linting: flake8

Local release (packaging/documentation) is also controlled by `Makefile`
- Docs: sphinx, readthedocs (rtd theme)
- Release: PyPI, twine, wheel

Remote tests to ensure that pullrequests contain good code:
- CI (testing/linting): github actions workflow
- CD (pypi release): github actions workflow

Shared collaboration standards:
- `.editorconfig`: configuration across different IDE's
- `contributing.md`: tutorial for contributors

---

Big parts of this cookiecutter are based on:
- [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
- [template-python](https://github.com/jacebrowning/template-python)
