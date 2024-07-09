from setuptools import find_packages,setup

setup(
    name='chat_with_postgres_db',
    version='0.0.1',
    author='shiva shankar',
    author_email='ji.shiva1998@Gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2","langchain-groq","langchain_community","psycopg2-binary"],
    packages=find_packages()
)