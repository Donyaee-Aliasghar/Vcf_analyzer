"""Module for reading VCF files."""

try:
    from cyvcf2 import VCF
except ImportError:
    raise ImportError("cyvcf2 is not installed. Please install it with 'pip install cyvcf2'.")
import pandas as pd


def read_file(file_path):
    """Read a VCF file and return its contents as a pandas DataFrame."""

    import os

    records = []

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        vcf = VCF(file_path)
    except Exception as e:
        print(f"[❌] Error opening VCF: {e}")
        raise

    for variant in vcf:
        alt = variant.ALT
        if isinstance(alt, (list, tuple)) and len(alt) > 0:
            alt_val = alt[0]
        else:
            alt_val = None
        rec = {
            "CHROM": variant.CHROM,
            "POS": variant.POS,
            "REF": variant.REF,
            "ALT": alt_val,
            "QUAL": variant.QUAL,
        }

        # Add allele frequency (AF) if available
        rec["AF"] = variant.INFO.get("AF") if "AF" in variant.INFO else None

        records.append(rec)

    print(f"[DEBUG] Read {len(records)} records from {file_path}")
    df = pd.DataFrame(records)
    return df
