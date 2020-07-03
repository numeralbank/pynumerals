from setuptools import setup, find_packages


setup(
    name='pynumerals',
    version='0.0',
    author='',
    author_email='lingweb@shh.mpg.de',
    url='https://github.com/numeralbank/pynumerals',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    python_requires='>=3.5',
    install_requires=[
        'attr',
        'beautifulsoup4>=4.6.3',
        'clldutils',
        'fuzzywuzzy',
        'pytest',
    ],
)
