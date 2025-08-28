"""
Setup script for Control Fintech
"""

from setuptools import setup, find_packages

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="control-fintech",
    version="1.0.0",
    author="Control Fintech Team",
    author_email="contato@controlfintech.com",
    description="Sistema de análise do impacto financeiro de decisões cotidianas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/control-fintech/control-fintech",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Education",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "control-fintech=scripts.gerar_resultados:main",
            "fintech-calc=src.opportunity_cost_calculator:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
