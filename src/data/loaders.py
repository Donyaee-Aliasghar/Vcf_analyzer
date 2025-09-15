"""Module for getting and opening VCF files."""

import gzip
from pathlib import Path


def open_vcf(path: Path):
    """Return handle for .vcf, .vcf.gz, or .vcf.bgz files."""
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    # Handle .vcf, .vcf.gz, .vcf.bgz
    suffixes = path.suffixes
    try:
        if suffixes[-2:] == [".vcf", ".gz"] or suffixes[-2:] == [".vcf", ".bgz"]:
            return gzip.open(path, "rt", encoding="utf-8")
        elif suffixes[-1] == ".vcf":
            return open(path, "r", encoding="utf-8")
        elif suffixes[-1] in [".gz", ".bgz"]:
            return gzip.open(path, "rt", encoding="utf-8")
        else:
            raise ValueError(f"Unsupported file type: {''.join(suffixes)}")
    except Exception as e:
        print(f"[❌] Error opening file {path}: {e}")
        raise
