"""Basic analyse of VCF file."""

import statistics

from ..data.routing import OUTPUT_BASIC_ANALYSE_DIR
from ..data.loaders import open_vcf
from .clean_vcf_line import clean_vcf_line


def main(input_pure_file):
    """Main operations."""

    total_variants = 0
    snps = 0
    indels = 0
    quals = []

    # Output file path.
    output_path = OUTPUT_BASIC_ANALYSE_DIR / "basic_analyse.txt"

    with open_vcf(input_pure_file) as fi, open(str(output_path), "w", encoding="utf-8") as fo:
        for line in fi:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                if clean_vcf_line(line):
                    fo.write(line + "\n")
                continue
            cols = line.split("\t")
            if len(cols) < 6:
                continue
            ref = cols[3]
            alt = cols[4]
            qual = cols[5]
            total_variants += 1
            if len(ref) == 1 and len(alt) == 1:
                snps += 1
            if len(ref) != len(alt):
                indels += 1
            try:
                quals.append(float(qual))
            except ValueError:
                pass
            if clean_vcf_line(line):
                fo.write(line + "\n")

        mean_qual = statistics.mean(quals) if quals else 0.0
        fo.write("=" * 20 + "📊 Variants statistics " + "=" * 20 + "\n")
        fo.write(f"Total variants: {total_variants}\n")
        fo.write(f"Number of SNPs: {snps}\n")
        fo.write(f"Number of InDels: {indels}\n")
        fo.write(f"Average quality: {mean_qual:.10f}\n")

    print("[✅] Basic analyse successful:", output_path)
