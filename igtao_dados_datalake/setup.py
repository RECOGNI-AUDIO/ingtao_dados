# setup.py

from setuptools import setup, find_packages

setup(
    name='igtao_dados_datalake',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'azure-storage-blob',
        'python-dotenv'
    ]
)