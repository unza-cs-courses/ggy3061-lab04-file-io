"""
Pytest configuration for Lab 4 visible tests.
"""

import json
import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def variant_config():
    """Load student's variant configuration."""
    config_path = Path(__file__).parent.parent.parent / ".variant_config.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    return {
        "parameters": {
            "num_records": 50,
            "locations": ["Site-A", "Site-B"],
            "depth_range": {"min": 50, "max": 500},
            "include_errors": 3
        }
    }
