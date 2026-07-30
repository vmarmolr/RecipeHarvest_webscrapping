# Practice 1 - Data Typology and Life Cycle

**Course:** M2.851 | **Semester:** 2024-1 | **Date:** 12-11-2024

## Authors

* Victor Marmol Romero - vmarmolro@uoc.edu
* Joan Sabaté Terrón - jsabatete@uoc.edu

## Data Source

https://www.3cat.cat/tv3/cuines/receptes/

## Dataset Publication

This dataset has been published on Zenodo: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14054272.svg)](https://doi.org/10.5281/zenodo.14054272)

## Repository Structure

This repository contains the following components:

- **`/dataset/`** - Extracted data from various cooking shows
  - `receptes.csv` - Complete dataset of recipes
  - `urls.txt` - URLs of all scraped recipe pages

- **`/source/`** - Source code
  - `Cuines.py` - Main scraper program
  - `requirements.txt` - Python dependencies
  - `Segmentacio/` - Testing and debugging scripts
    - `Desdeurl.py` - Generates `receptes.csv` from `urls.txt`
    - `PasapaginesCuines.py` - Tests dynamic pagination handling
    - `UnaRecepta.py` - Extracts and validates individual recipes

## Getting Started

### Requirements

- Internet connection
- Python 3.x
- One of the following browsers installed:
  - Microsoft Edge
  - Google Chrome

### Installation

```bash
pip install -r source/requirements.txt
```

### Running the Scraper

Execute the main script to generate the dataset:

```bash
python source/Cuines.py
```

This will:
1. Generate `urls.txt` with all recipe URLs
2. Create `receptes.csv` with the complete dataset (~8,000 recipes)

### Important Notes

- **Execution Time:** The scraper takes considerable time to run due to the large dataset size and dynamic pagination handling
- **Dynamic Pagination:** The website uses JavaScript-based pagination, which requires special handling
- **Error Handling:** The `Segmentacio/UnaRecepta.py` script can be used to debug individual recipes that encounter errors
- **Documentation:** See the accompanying PDF report for detailed technical implementation details

## Troubleshooting

If you encounter issues with dynamic page loading, refer to `PasapaginesCuines.py` to understand the pagination behavior.

For individual recipe extraction problems, use `UnaRecepta.py` with a specific recipe URL to test and validate.

---

*For complete technical details and methodology, please refer to the project documentation (PDF).*
