"""Module for visualizing VCF data."""

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
from ..advanced_analyse.read_file import read_file
from ..data.routing import OUTPUT_ADVANCED_ANALYSE_DIR


def visualize_data(data):
    """Visualize the given VCF data."""

    df = read_file(data)

    # Chromosomal distribution
    chrom_counts = df["CHROM"].value_counts().sort_index()

    plt.figure(figsize=(12, 6))
    sns.barplot(x=chrom_counts.index, y=chrom_counts.values, palette="viridis")
    plt.title("Variant Distribution Across Chromosomes")
    plt.xlabel("Chromosome")
    plt.ylabel("Number of Variants")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_ADVANCED_ANALYSE_DIR}/chromosomal_distribution.png")
    plt.close()

    # Allele frequency distribution
    if df["AF"].notnull().any():
        plt.figure(figsize=(10, 6))
        sns.histplot(df["AF"].dropna(), bins=50, kde=True, color="skyblue")
        plt.title("Allele Frequency Distribution")
        plt.xlabel("Allele Frequency")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_ADVANCED_ANALYSE_DIR}/allele_frequency_distribution.png")
        plt.close()

    # QUAL filtering
    qual_threshold = 30
    filtered = df[df["QUAL"] >= qual_threshold]

    plt.figure(figsize=(8, 5))
    sns.histplot(df["QUAL"], bins=50, color="red", alpha=0.5, label="All Variants")
    sns.histplot(filtered["QUAL"], bins=50, color="green", alpha=0.5, label="QUAL >= 30")
    plt.title("QUAL Distribution (Before/After Filtering)")
    plt.xlabel("QUAL")
    plt.ylabel("Count")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_ADVANCED_ANALYSE_DIR}/qual_filtering.png")
    plt.close()

    # Output to csv
    summary = {
        "total_variants": len(df),
        "high_quality_variants": len(filtered),
        "mean_qual": df["QUAL"].mean(),
        "mean_af": df["AF"].mean(skipna=True),
    }
    pd.DataFrame([summary]).to_csv(f"{OUTPUT_ADVANCED_ANALYSE_DIR}/vcf_data.csv", index=False)

    print(f"[✅] Advanced analysis and visualizations complete. : {OUTPUT_ADVANCED_ANALYSE_DIR}")
