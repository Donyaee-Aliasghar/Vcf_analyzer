"""Module for cleaning vcf line."""


def clean_vcf_line(line: str) -> bool:
    """Operations."""
    line = line.strip()
    if line == "":
        return False
    if line.startswith("##"):
        return False
    return True
