# /usr/bin/env python3

# setup.py - Setup source file of lsprotein
# Written by Ercan Ersoy (http://ercanersoy.net).

import lsprotein.version
from setuptools import setup, find_packages

setup(
    name='lsprotein',
    description='Protein lister on command line interface',
    long_description='Protein lister on command line interface',
    keywords='protein ls lister pdb protein-data-bank protein-database \
    rest-api command-line cli command-line-interface',
    version=lsprotein.version.lsprotein_version,
    author='Ercan Ersoy',
    author_email='ercanersoy@ercanersoy.net',
    maintainer='Ercan Ersoy',
    maintainer_email='ercanersoy@ercanersoy.net',
    url='https://github.com/ercanersoy/lsprotein',
    license='MIT',
    packages=['lsprotein'],
    scripts=['bin/lsprotein'],
    install_requires=['beautifulsoup4'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)
