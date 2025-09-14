"""Module for get and open VCF files."""

import gzip

from pathlib import Path


def open_vcf(path: Path):
    """Return .vcf.gz or .vcf."""
    if path.suffix == ".gz":
        return gzip.open(path, "rt")  # text mode
    else:
        return open(path, "r")
