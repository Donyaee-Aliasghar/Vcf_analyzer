"""Module for routing."""

from pathlib import Path

# Root dir.
ROOT_DIR = Path(__file__).resolve().parents[2]

# Results dir.
RESULTS_DIE = ROOT_DIR / "results"

# Output dir for purified raw data.
OUTPUT_PURIFIED_DATA_DIR = RESULTS_DIE / "data/purified"
OUTPUT_PURIFIED_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Output dir for basic analyse.
OUTPUT_BASIC_ANALYSE_DIR = RESULTS_DIE / "basic_analyse"
OUTPUT_BASIC_ANALYSE_DIR.mkdir(parents=True, exist_ok=True)

# Get pure file of results directory.
vcf_files = list(OUTPUT_PURIFIED_DATA_DIR.glob("*.vcf"))
if vcf_files:
    INPUT_PURE_FILE = vcf_files[0]
else:
    INPUT_PURE_FILE = None
    print(f"[❌] No .vcf file found in {OUTPUT_PURIFIED_DATA_DIR}")

# Output dir for advanced analyse.
OUTPUT_ADVANCED_ANALYSE_DIR = RESULTS_DIE / "advanced_analyse"
OUTPUT_ADVANCED_ANALYSE_DIR.mkdir(parents=True, exist_ok=True)
