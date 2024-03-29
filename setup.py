from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Flask-PostgreSQL",
    version="1.1.1",
    author="Aleksandrs Kašs",
    author_email="aleksandrs.kass@gmail.com",
    description="Flask extension for PostgreSQL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kashcode/flask-postgresql",
    packages=find_packages(),
    platforms='any',
    install_requires=['Flask'],
    extras_require={
        "dev": [
            "pytest>=6.2",
            "twine>=3.3.0",
            "pytest-dotenv>=0.5.2",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
