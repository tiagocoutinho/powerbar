# -*- coding: utf-8 -*-

"""The setup script."""

import sys
from setuptools import setup, find_packages


TESTING = any(x in sys.argv for x in ["test", "pytest"])

requirements = ['wcwidth', 'blessings']

setup_requirements = []
if TESTING:
    setup_requirements += ['pytest-runner']
test_requirements = ['pytest', 'pytest-cov']

setup(
    name='powerbar',
    author="Jose Tiago Macara Coutinho",
    author_email='coutinhotiago@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    description="TLI progress bar",
    install_requires=requirements,
    license="LGPL3+",
    long_description="TLI bars (vbar, progress bar, spark)",
    keywords='progress, bar, ascii, TLI, CLI',
    packages=find_packages(include=['powerbar']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    python_requires='>=3.5',
    url='https://gitlab.com/tiagocoutinho/powerbar',
    version='0.1.0',
    zip_safe=True
)
