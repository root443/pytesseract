from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='fasita',
    version='0.0.1',
    install_requires=requirements,
    long_description=long_description,
    packages=find_packages(exclude=("input", "output",)),
    entry_points = {
        'console_scripts': [
            'fasita = fasita.ocr:main',
            'fasita-makeboxes = fasita.makeboxes:main',
            'fasita-test = fasita.settings.test:main'
        ]
    },
    include_package_data=True,
)
