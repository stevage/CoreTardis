import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="MicroTardis-filters",
    version="0.1",
    url='https://github.com/stevage/MicroTardis-filters',
    license='WTFPL',
    description="A couple of microscopy filters for MyTardis (.spc and .tif)",
    author='Joanna Huang, Ian Thomas, Steve Bennett',
    author_email='steve.bennett@versi.edu.au',
    packages=find_packages(),
    namespace_packages=['tardis.apps'],
    install_requires=[
        'PIL>=1.1.7',
        'numpy'
        ],
)
