# Variant Call Format(VCF) analyzer
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
## Title
A tool for cleaning, parsing, interpreting and analyzing vcf files.

## Description 
This project provides a comprehensive solution for working with Variant Call Format (VCF) files, which are widely used in bioinformatics for storing gene sequence variations. The VCF analyzer simplifies the process of cleaning, parsing, interpreting, and analyzing VCF files, making it easier for researchers and developers to extract meaningful insights from genetic data. With an intuitive interface and robust features, this tool is suitable for both beginners and advanced users working with genomic datasets.

## Features
- Clean and filter VCF files to remove unwanted variants
- Parse VCF files and extract relevant information (e.g., sample genotypes, variant annotations)
- Summarize variant statistics (e.g., counts, frequencies, quality metrics)
- Support for both uncompressed `.vcf` and compressed `.vcf.gz` and `.vcf.bgz` files
- Command-line interface for easy interaction
- Export results to various formats (CSV, TXT)
- Modular and extensible codebase for custom analyses
- User-friendly error handling and informative messages
- Compatible with Python 3.x and Poetry for dependency management

## Installation 
1.Cloning this project
```bash
https://github.com/Donyaee-Aliasghar/Vcf_analyzer.git
```
2.Go to the Vcf_analyzer
```bash
cd Vcf_analyzer
```
3.Install the packages
>⚠️ Make sure you have peotry on your system.
```python
poetry install
```

## Usage
1.Go to the Vcf_analyzer
```bash
cd Vcf_analyzer/src
```
2.Run the following code
```python
python -i <input vsc file(.vcf or .vcf.gz)> cli.py
```

## Project structure
.
├── pyproject.toml
├── README.md
├── results
│   ├── advanced_analyse/
│   │   
│   ├── basic_analyse/
│   │   
│   └── data
│       └── purified/
│           
├── src
│   ├── advanced_analyse
│   │   └── read_file.py
│   ├── basic_analyse
│   │   ├── clean_vcf_line.py
│   │   ├── main.py
│   │       
│   ├── cli.py
│   ├── data
│   │   ├── loaders.py
│   │   ├── purification.py
│   │   └── routing.py
│   ├── __init__.py
│   ├── runner.py
│   └── visualization
│       ├── main.py
│
└── tests
    └── __init__.py

## License
Free to use 😊
