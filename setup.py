from setuptools import setup, find_packages


setup(
    name='pynumerals',
    version='1.0.0.dev0',
    license='Apache 2.0',
    description='Helper library for numeralbank projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    author='Hans-Jörg Bibiko, Christoph Rzymski, Robert Forkel',
    keywords='data',
    author_email='lingweb@shh.mpg.de',
    url='https://github.com/numeralbank/pynumerals',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "cldfbench.commands": [
            "pynumerals=pynumerals.commands",
        ]
    },
    platforms='any',
    python_requires='>=3.5',
    install_requires=[
        'attr',
        'beautifulsoup4>=4.9.1',
        'clldutils>=3.5.4',
        'pylexibank>=2.8.2',
        'openpyxl>=3.0.5',
        'python-levenshtein>=0.12',
        'fuzzywuzzy>=0.18',
    ],
    extras_require={
        'dev': ['flake8', 'wheel', 'twine'],
        'test': [
            'pytest>=6.0.2',
            'pytest-mock>=3.3.1',
            'pytest-cov>=2.10.1',
            'coverage>=5.3',
            'pyglottolog>=3.2.2',
        ],
    },
)
