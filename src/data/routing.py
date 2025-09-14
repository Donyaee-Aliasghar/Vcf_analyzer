"""Module for routing."""

from pathlib import Path

# Output dir for purified raw data.
OUTPUT_PURIFIED_DATA_DIR = Path(__file__).resolve().parents[2] / "results/data/purified"
OUTPUT_PURIFIED_DATA_DIR.mkdir(parents=True, exist_ok=True)
