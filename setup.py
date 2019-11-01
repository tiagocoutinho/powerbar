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

with open('README.md') as f:
    description = f.read()

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
    license="GPLv3+",
    description="Concurrency agnostic socket API",
    long_description=description,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    keywords='progress, bar, ASCII, TLI, CLI',
    packages=find_packages(include=['powerbar']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    python_requires='>=3.5',
    url='https://github.com/tiagocoutinho/powerbar',
    version='0.1.0',
    zip_safe=True
)
