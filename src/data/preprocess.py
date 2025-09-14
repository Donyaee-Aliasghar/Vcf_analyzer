"""Module for purification VCF file."""

from .routing import RAW_VCF_FILE, OUTPUT_PURIFIED_DATA_DIR
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


for vcf_file in RAW_VCF_FILE:
    clean_file = OUTPUT_PURIFIED_DATA_DIR / ("pure_" + vcf_file.stem + ".vcf")
    with open_vcf(vcf_file) as fr, open(clean_file, "w") as fw:
        print("[✅] Open raw VCF file successful.")
        for line in fr:
            if clean_vcf_line(line):
                fw.write(line)
        print(f"[✅] Purified VCF file successful. {clean_file}")
