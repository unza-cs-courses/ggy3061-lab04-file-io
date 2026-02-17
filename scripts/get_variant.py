#!/usr/bin/env python3
"""
Deterministic Variant Computation - Lab 4: File I/O

Run this script to see YOUR unique assignment values:
    python scripts/get_variant.py
"""

import hashlib
import random
import json
import os
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional

SEED_SALT = "GGY3061_2026"
ASSIGNMENT_ID = "lab04"
VARIANT_STRATEGY = "grouped"
NUM_GROUPS = 10


def compute_seed(student_id: str) -> int:
    combined = f"{ASSIGNMENT_ID}:{SEED_SALT}:{student_id}"
    hash_bytes = hashlib.sha256(combined.encode()).digest()
    return int.from_bytes(hash_bytes[:8], byteorder='big')


def _get_csv_locations():
    """Read actual locations from samples.csv to avoid mismatch."""
    import csv as _csv
    csv_path = Path(__file__).resolve().parent.parent / "data" / "samples.csv"
    locations = set()
    try:
        with open(csv_path, newline="") as f:
            reader = _csv.DictReader(f)
            for row in reader:
                loc = row.get("location", "").strip()
                if loc:
                    locations.add(loc)
    except Exception:
        # Fallback if CSV cannot be read (e.g., during CI before checkout)
        locations = {"Site-A", "Site-B"}
    return sorted(locations)


def generate_parameters(rng, group_id):
    all_sites = _get_csv_locations()
    min_d = rng.randint(50, 150)
    num_locations = min(rng.randint(2, 4), len(all_sites))
    return {
        'num_records': rng.randint(40, 60),
        'locations': rng.sample(all_sites, k=num_locations),
        'depth_range': {'min': min_d, 'max': min_d + rng.randint(300, 500)},
        'include_errors': rng.randint(2, 5),
    }


def get_variant_for_student(student_id: str) -> Dict[str, Any]:
    seed = compute_seed(student_id)
    group_id = seed % NUM_GROUPS
    rng = random.Random(seed)
    parameters = generate_parameters(rng, group_id)
    return {
        'student_id': student_id,
        'variant_seed': seed,
        'group_id': group_id,
        'parameters': parameters
    }


def get_repo_name() -> Optional[str]:
    github_repo = os.environ.get('GITHUB_REPOSITORY')
    if github_repo:
        return github_repo.split('/')[-1]
    try:
        result = subprocess.run(['git', 'remote', 'get-url', 'origin'],
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return result.stdout.strip().rstrip('.git').split('/')[-1]
    except:
        pass
    return Path.cwd().name


def get_my_username() -> str:
    repo_name = get_repo_name()
    if repo_name:
        parts = repo_name.split('-')
        return parts[-1] if len(parts) > 1 else repo_name
    return "unknown"


def get_my_variant() -> Dict[str, Any]:
    return get_variant_for_student(get_my_username())


if __name__ == "__main__":
    variant = get_my_variant()
    params = variant['parameters']
    
    print("=" * 60)
    print("YOUR ASSIGNMENT VALUES - Lab 4: File I/O")
    print("=" * 60)
    print(f"\nStudent: {variant['student_id']}")
    print(f"Variant Group: {variant['group_id']}")
    print()
    print("Use these EXACT values in your code:")
    print("-" * 40)
    for key, value in params.items():
        print(f"  {key} = {repr(value)}")
    print("-" * 40)
    print()
    print("Using someone else's values = FAIL on hidden tests")
