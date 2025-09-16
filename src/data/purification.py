"""Module for purification VCF file."""

from .routing import OUTPUT_PURIFIED_DATA_DIR
from .loaders import open_vcf


def clean_vcf_line(line: str) -> bool:
    """Operations."""
    line = line.strip()

    # Delete empty line.
    if line == "":
        return False

    # Save header and variants.
    if line.startswith("##") or line.startswith("#CHROM") or not line.startswith("#"):
        return True

    return False


def process_vcf(input_paths):
    """Process VCF file."""
    clean_file = OUTPUT_PURIFIED_DATA_DIR / ("purified_" + input_paths.name + ".vcf")
    with open_vcf(input_paths) as fr, open(clean_file, "w", encoding="utf-8") as fw:
        print("[✅] Open raw VCF file successful.")
        for line in fr:
            if clean_vcf_line(line):
                fw.write(line)
        print(f"[✅] Purified VCF file successful. {clean_file}")
