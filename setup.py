#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="UGridViz",
    version="0.1a",
    packages=find_packages(),
    scripts=['ugridviz.py', ],
    install_requires=['docutils', ],
    package_data={'': ['*.cfg', '*.txt', '*.rst', '*.md', ], },
    author="Chris Calloway",
    author_email="cbc@chriscalloway.org",
    description="A client for the discovery and vizualization of data conforming to UGRID conventions.",
    license="GPL2",
    keywords="NHC RENCI ugrid ADCIRC unstructured grid hurricane model tropical storm",
    url="https://github.com/renci-unc/ugridviz",
    long_description=open('README.rst', 'r').read(),
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                 'Topic :: Scientific/Engineering :: Atmospheric Science', ]
    )
