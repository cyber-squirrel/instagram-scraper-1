# -*- coding: utf-8 -*-
from pathlib import Path

import setuptools

setuptools.setup(
    name='igramscraper',
    version='0.3.5',
    description=('scrapes medias, likes, followers, tags and all metadata'),
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    license='MIT',
    maintainer='realsirjoe, leungwaiban',
    author='realsirjoe, leungwaiban',
    url='https://github.com/realsirjoe/instagram-scraper',
    install_requires=['python==^3.9', 'requests==^2.25.0', 'python-slugify==^4.0.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
    ],
)
