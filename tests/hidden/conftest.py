"""
Pytest configuration for Lab 4 hidden tests.
"""

import csv
import json
import sys
import importlib.util
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Path setup
# ---------------------------------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
SRC_DIR = ROOT_DIR / "src"
DATA_DIR = ROOT_DIR / "data"

sys.path.insert(0, str(SRC_DIR))


# ---------------------------------------------------------------------------
# Variant configuration
# ---------------------------------------------------------------------------
@pytest.fixture(scope="session")
def variant_config():
    """Load student's variant configuration from .variant_config.json or fall
    back to computing it via get_variant.py."""
    config_path = ROOT_DIR / ".variant_config.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    # Fall back: import get_variant.py dynamically
    spec = importlib.util.spec_from_file_location(
        "get_variant", str(ROOT_DIR / "scripts" / "get_variant.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.get_my_variant()


@pytest.fixture(scope="session")
def variant_params(variant_config):
    """Shortcut to the parameters dict inside variant_config."""
    return variant_config.get("parameters", variant_config)


@pytest.fixture(scope="session")
def variant_locations(variant_params):
    """List of locations from the variant."""
    return variant_params["locations"]


@pytest.fixture(scope="session")
def variant_depth_range(variant_params):
    """Depth range dict with 'min' and 'max'."""
    return variant_params["depth_range"]


@pytest.fixture(scope="session")
def variant_num_records(variant_params):
    """Number of records parameter."""
    return variant_params["num_records"]


@pytest.fixture(scope="session")
def variant_include_errors(variant_params):
    """Number of error rows parameter."""
    return variant_params["include_errors"]


# ---------------------------------------------------------------------------
# CSV data fixtures
# ---------------------------------------------------------------------------
@pytest.fixture(scope="session")
def samples_csv_path():
    """Absolute path to data/samples.csv."""
    return str(DATA_DIR / "samples.csv")


@pytest.fixture(scope="session")
def sample_csv_data(samples_csv_path):
    """Load CSV data as list of dicts (session-scoped to avoid repeated I/O)."""
    with open(samples_csv_path, newline="") as f:
        return list(csv.DictReader(f))


@pytest.fixture
def alternative_csv_data(tmp_path):
    """Create a temporary CSV with different data to catch hardcoded values."""
    alt_path = tmp_path / "alt_samples.csv"
    header = ["sample_id", "rock_type", "grade", "depth", "mass", "location"]
    rows = [
        ["ALT-001", "Marble", "1.1", "110", "8.0", "Site-A"],
        ["ALT-002", "Quartzite", "4.5", "320", "20.0", "Site-B"],
        ["ALT-003", "Gneiss", "2.9", "200", "14.2", "Site-A"],
        ["ALT-004", "Slate", "0.3", "50", "6.5", "Site-B"],
        ["ALT-005", "Marble", "3.7", "410", "17.8", "Site-A"],
    ]
    with open(alt_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    return str(alt_path)


# ---------------------------------------------------------------------------
# Temp directory fixture
# ---------------------------------------------------------------------------
@pytest.fixture
def temp_dir(tmp_path):
    """Provide a temporary directory for file output tests."""
    return tmp_path
