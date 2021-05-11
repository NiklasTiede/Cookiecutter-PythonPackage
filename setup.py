# !/usr/bin/env python

import setuptools
import pathlib

setuptools.setup(
    name='cookiecutter-NiklasPyPackage',
    version='0.1.0',
    author='Niklas Tiede',
    author_email='niklastiede2@gmail.com',
    description="Cookiecutter template for a Python package Niklas' style",
    url='https://github.com/niklastiede/cookiecutter-NiklasPyPackage',
    license='MIT',

    packages=[],

    keywords=['cookiecutter', 'template', 'package'],
    python_requires='>=3.6',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
)

