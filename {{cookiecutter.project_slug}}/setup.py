"""The setup script."""

import pathlib
import re
from setuptools import find_packages
from setuptools import setup
from typing import Any
from typing import Union


def get_value(variable: str) -> Union[str, Any]:
    """ Direct import of metadata would invoke a ModuleNotFoundError for 3rd party package
    libraries when installing this project for development.
    """
    content = pathlib.Path(
        "src/{{ cookiecutter.project_slug }}/__init__.py").read_text(encoding="utf-8")
    pattern = f'^{variable} = [\'"]([^\'\"]*)[\'"]'
    raw_s = r'{}'.format(pattern)
    p = re.compile(raw_s, re.M)
    return p.search(content).group(1)  # type: ignore


{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}


setup(
    name='{{ cookiecutter.project_slug }}',
    version=get_value('__version__'),
    author=get_value('__author__'),
    author_email=get_value('__email__'),
    {%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
    {%- endif %}
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=pathlib.Path(
        "pypidocs.md").read_text(encoding="utf-8"),
    long_description_content_type='text/markdown',
    project_urls={
        'Documentation': 'https://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/',
        'Source Code': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires='>=3.6',
    install_requires=[
        {%- if cookiecutter.command_line_interface|lower == 'click' %}'Click>=7.0',{%- endif %}
    ],
    extras_require={         # pip install -e .[dev]
        "dev": [
            "pytest",
            "pytest-cov",
            "tox",
            "pre-commit",
        ],
    },
    platforms="any",
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main',
        ],
    },
    {%- endif %}
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
