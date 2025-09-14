"""Module for routing raw data."""

import re

from pathlib import Path


# =============== Get raw file ==================

# My system path.--------------------------------
RAW_FILE_DIR = Path(__file__).resolve().parents[6] / "Raw_datas" / "Bioinformatics" / "VCF"
RAW_VCF_FILE = [f for f in RAW_FILE_DIR.glob("*") if re.match(r".*\.vcf(\.gz)?$", f.name)]

# Program path.----------------------------------
# RAW_FILE_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"
# RAW_VCF_FILE = [f for f in RAW_FILE_DIR.glob("*") if re.match(r".*\.vcf(\.gz)?$", f.name)]

# ===============================================

# Output dir for purified raw data.
OUTPUT_PURIFIED_DATA_DIR = Path(__file__).resolve().parents[2] / "results/data/purified"
OUTPUT_PURIFIED_DATA_DIR.mkdir(parents=True, exist_ok=True)
