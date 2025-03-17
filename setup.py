from setuptools import find_packages, setup


setup(
    name='mcq_generator',
    version='0.0.1',
    author='krunal shinde',
    author_email='krunals27920@gmail.com',
    install_requires=['ipykernel','langchain','langchain-openai','langchain-community','PyPDF2','python-dotenv','pandas','streamlit'],
    packages=find_packages()
)