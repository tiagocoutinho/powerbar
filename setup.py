# -*- coding: utf-8 -*-

"""The setup script."""

import sys
from setuptools import setup, find_packages


if sys.version_info < (3, 6):
    print('progbar needs python >= 3.6')
    exit(1)

TESTING = any(x in sys.argv for x in ["test", "pytest"])

requirements = ['wcwidth']

setup_requirements = []
if TESTING:
    setup_requirements += ['pytest-runner']
test_requirements = ['pytest', 'pytest-cov']
extras_requirements = {
}

setup(
    name='progbar',
    author="Jose Tiago Macara Coutinho",
    author_email='coutinhotiago@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    description="TLI progress bar",
    install_requires=requirements,
    license="MIT license",
    long_description="TLI progress bar",
    keywords='progress, TLI, CLI',
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    extras_require=extras_requirements,
    url='https://gitlab.com/tiagocoutinho/progbar',
    version='0.1.0',
    zip_safe=True
)
