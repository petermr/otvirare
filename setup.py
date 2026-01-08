#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path

from setuptools import setup

# Read version from __init__.py
import re

parent = Path(__file__).parent
with open(str(Path(parent, "otvirare", "__init__.py"))) as f:
    content = f.read()
version = re.search(r'__version__ = ["\']([^"\']+)["\']', content).group(1)

# Read README
try:
    with open('README.md', encoding='utf-8') as readme_file:
        readme = readme_file.read()
except FileNotFoundError:
    readme = "otvirare: Convert scientific research institution annual reports to structured semantic HTML"

requirements = [
    'lxml',
    'requests',
]

setup(
    name='otvirare',
    version=version,
    description='Convert scientific research institution annual reports to structured semantic HTML',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Otvirare Team',
    python_requires='>=3.8',
    packages=['otvirare'],
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'black',
            'flake8',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering',
    ],
)

