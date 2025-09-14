"""This module is for executing all the different parts of the code in one place."""

import argparse

from pathlib import Path

from Projects.Python_language.Personal.Vcf_analyzer.src.data.purification import process_vcf


def runner():
    """Collection location."""

    # Set input commands.
    parser = argparse.ArgumentParser(description="🧬 VCF file analyzer (basic filtering)")
    parser.add_argument("-i", "--input", required=True, help="Input file path.(vcf or vcf.gz)")

    args = parser.parse_args()

    input_path = Path(args.input)

    # Cleaned vcf file operations.
    process_vcf(input_path)

    args = parser.parse_args()

    # Input file check.
    if not input_path.exists():
        raise FileNotFoundError(f"[❌] Inputed file not found : {input_path}")

    print("[✅] Pure VCF file found >>> reading file...")
    print("[✅] Start operations...")

    # ...
