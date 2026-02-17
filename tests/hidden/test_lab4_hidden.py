"""
Lab 4 Hidden Tests - File I/O & CSV Processing
These tests validate deeper correctness and use variant-specific parameters.
~34 tests across 7 test classes.
"""

import csv
import os
import sys
from pathlib import Path

import pytest

SRC_DIR = Path(__file__).resolve().parent.parent.parent / "src"
DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
sys.path.insert(0, str(SRC_DIR))


# ========================================================================
# TestHiddenTextIO  (~5 tests)
# ========================================================================


class TestHiddenTextIO:
    """Hidden tests for lab4_text_io.py functions."""

    def test_write_and_read_sample_log_roundtrip(self, temp_dir):
        """write_sample_log then read_sample_log should produce consistent data."""
        from lab4_text_io import write_sample_log, read_sample_log

        samples = [
            {"id": "HID-001", "rock_type": "Gneiss", "grade": 3.14},
            {"id": "HID-002", "rock_type": "Slate", "grade": 0.72},
        ]
        path = str(temp_dir / "roundtrip.txt")
        lines_written = write_sample_log(path, samples)
        # header + separator + 2 sample lines = 4
        assert lines_written == 4, f"Expected 4 lines written, got {lines_written}"

        sample_lines = read_sample_log(path)
        assert len(sample_lines) == 2, "read_sample_log should return 2 sample lines"
        assert "HID-001" in sample_lines[0]
        assert "Gneiss" in sample_lines[0]
        assert "HID-002" in sample_lines[1]

    def test_append_to_log_preserves_original(self, temp_dir):
        """append_to_log should add content without destroying existing lines."""
        from lab4_text_io import write_sample_log, append_to_log, count_lines

        samples = [{"id": "APP-001", "rock_type": "Basalt", "grade": 2.0}]
        path = str(temp_dir / "append_test.txt")
        write_sample_log(path, samples)
        original_count = count_lines(path)

        append_to_log(path, "Extra line 1")
        append_to_log(path, "Extra line 2")
        new_count = count_lines(path)
        assert new_count == original_count + 2, (
            f"Expected {original_count + 2} lines after 2 appends, got {new_count}"
        )

    def test_count_lines_known_file(self, temp_dir):
        """count_lines should return the exact number of lines."""
        from lab4_text_io import write_lines, count_lines

        path = str(temp_dir / "count_test.txt")
        lines = ["alpha", "beta", "gamma", "delta", "epsilon"]
        write_lines(path, lines)
        assert count_lines(path) == 5

    def test_read_file_content_and_write_lines(self, temp_dir):
        """write_lines and read_file_content should be consistent."""
        from lab4_text_io import write_lines, read_file_content

        path = str(temp_dir / "content_test.txt")
        original = ["Rock sample A", "Rock sample B"]
        write_lines(path, original)
        content = read_file_content(path)
        assert isinstance(content, str)
        assert "Rock sample A" in content
        assert "Rock sample B" in content

    def test_write_sample_log_with_variant_data(self, temp_dir, variant_num_records):
        """write_sample_log should handle a number of records from the variant."""
        from lab4_text_io import write_sample_log, count_lines

        num = min(variant_num_records, 10)  # limit for speed
        samples = [
            {"id": f"VAR-{i:03d}", "rock_type": "Granite", "grade": 1.0 + i * 0.1}
            for i in range(num)
        ]
        path = str(temp_dir / "variant_log.txt")
        lines_written = write_sample_log(path, samples)
        assert lines_written == num + 2, (
            f"Expected {num + 2} lines (header+sep+{num} samples), got {lines_written}"
        )
        assert count_lines(path) == lines_written


# ========================================================================
# TestHiddenCSVReader  (~6 tests)
# ========================================================================


class TestHiddenCSVReader:
    """Hidden tests for lab4_csv_reader.py functions."""

    def test_read_samples_as_list_actual_csv(self, samples_csv_path):
        """read_samples_as_list should return 51 rows (1 header + 50 data)."""
        from lab4_csv_reader import read_samples_as_list

        result = read_samples_as_list(samples_csv_path)
        assert isinstance(result, list)
        assert len(result) == 51, f"Expected 51 rows, got {len(result)}"
        assert result[0][0] == "sample_id"

    def test_read_samples_as_dict_keys(self, samples_csv_path):
        """read_samples_as_dict rows should have the 6 expected keys."""
        from lab4_csv_reader import read_samples_as_dict

        result = read_samples_as_dict(samples_csv_path)
        expected_keys = {"sample_id", "rock_type", "grade", "depth", "mass", "location"}
        assert set(result[0].keys()) == expected_keys
        assert len(result) == 50

    def test_get_column_values_grade(self, samples_csv_path):
        """get_column_values for 'grade' should return 50 string values."""
        from lab4_csv_reader import get_column_values

        grades = get_column_values(samples_csv_path, "grade")
        assert len(grades) == 50
        # All should be convertible to float
        for g in grades:
            float(g)

    def test_get_unique_values_location(self, samples_csv_path):
        """get_unique_values on 'location' should return {'Site-A', 'Site-B'}."""
        from lab4_csv_reader import get_unique_values

        locations = get_unique_values(samples_csv_path, "location")
        assert isinstance(locations, set)
        assert locations == {"Site-A", "Site-B"}

    def test_get_row_count_actual_csv(self, samples_csv_path):
        """get_row_count should return exactly 50."""
        from lab4_csv_reader import get_row_count

        assert get_row_count(samples_csv_path) == 50

    def test_find_rows_by_value_variant_location(
        self, samples_csv_path, variant_locations, sample_csv_data
    ):
        """find_rows_by_value should match the expected count for a variant location."""
        from lab4_csv_reader import find_rows_by_value

        loc = variant_locations[0]
        expected = sum(1 for r in sample_csv_data if r["location"] == loc)
        result = find_rows_by_value(samples_csv_path, "location", loc)
        assert len(result) == expected, (
            f"Expected {expected} rows for {loc}, got {len(result)}"
        )


# ========================================================================
# TestHiddenCSVWriter  (~5 tests)
# ========================================================================


class TestHiddenCSVWriter:
    """Hidden tests for lab4_csv_writer.py functions."""

    def test_write_samples_from_list_creates_valid_csv(self, temp_dir):
        """write_samples_from_list should produce a readable CSV."""
        from lab4_csv_writer import write_samples_from_list

        path = str(temp_dir / "wlist.csv")
        header = ["sample_id", "rock_type", "grade"]
        rows = [
            ["HID-001", "Marble", "1.5"],
            ["HID-002", "Quartzite", "3.9"],
            ["HID-003", "Gneiss", "2.2"],
        ]
        count = write_samples_from_list(path, header, rows)
        assert count == 3
        with open(path, newline="") as f:
            reader = csv.reader(f)
            all_rows = list(reader)
        assert all_rows[0] == header
        assert len(all_rows) == 4  # header + 3 data

    def test_write_samples_from_dict_creates_valid_csv(self, temp_dir):
        """write_samples_from_dict should produce a readable CSV."""
        from lab4_csv_writer import write_samples_from_dict

        path = str(temp_dir / "wdict.csv")
        fieldnames = ["sample_id", "rock_type", "grade"]
        rows = [
            {"sample_id": "HID-010", "rock_type": "Slate", "grade": "0.8"},
            {"sample_id": "HID-011", "rock_type": "Basalt", "grade": "4.2"},
        ]
        count = write_samples_from_dict(path, fieldnames, rows)
        assert count == 2
        with open(path, newline="") as f:
            data = list(csv.DictReader(f))
        assert len(data) == 2
        assert data[0]["sample_id"] == "HID-010"

    def test_filter_and_save_correct_filtering(self, alternative_csv_data, temp_dir):
        """filter_and_save should correctly filter by numeric threshold."""
        from lab4_csv_writer import filter_and_save

        output = str(temp_dir / "filtered.csv")
        # alt grades: 1.1, 4.5, 2.9, 0.3, 3.7 -- >= 3.0: 4.5, 3.7 => 2 rows
        count = filter_and_save(alternative_csv_data, output, "grade", 3.0)
        assert count == 2
        with open(output, newline="") as f:
            rows = list(csv.DictReader(f))
        assert len(rows) == 2
        ids = {r["sample_id"] for r in rows}
        assert "ALT-002" in ids
        assert "ALT-005" in ids

    def test_append_row_to_csv_adds_row(self, alternative_csv_data):
        """append_row_to_csv should increase row count by 1."""
        from lab4_csv_writer import append_row_to_csv

        new_row = {
            "sample_id": "ALT-099",
            "rock_type": "Dolomite",
            "grade": "2.2",
            "depth": "175",
            "mass": "12.0",
            "location": "Site-A",
        }
        result = append_row_to_csv(alternative_csv_data, new_row)
        assert result is True
        with open(alternative_csv_data, newline="") as f:
            rows = list(csv.DictReader(f))
        assert len(rows) == 6  # was 5 + 1 appended
        assert rows[-1]["sample_id"] == "ALT-099"

    def test_merge_csv_files_combines(self, temp_dir):
        """merge_csv_files should combine rows from multiple files."""
        from lab4_csv_writer import merge_csv_files

        paths = []
        for i, ids in enumerate([["M-001", "M-002"], ["M-003"]]):
            p = str(temp_dir / f"merge_{i}.csv")
            with open(p, "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["sample_id", "grade"])
                for sid in ids:
                    w.writerow([sid, "1.0"])
            paths.append(p)

        out = str(temp_dir / "merged.csv")
        total = merge_csv_files(paths, out)
        assert total == 3
        with open(out, newline="") as f:
            data = list(csv.DictReader(f))
        assert len(data) == 3


# ========================================================================
# TestHiddenDataProcessor  (~6 tests)
# ========================================================================


class TestHiddenDataProcessor:
    """Hidden tests for lab4_data_processor.py functions."""

    def test_calculate_statistics_actual_csv(self, samples_csv_path, sample_csv_data):
        """calculate_statistics on the real CSV should match hand-computed values."""
        from lab4_data_processor import calculate_statistics

        result = calculate_statistics(samples_csv_path, "grade")
        assert isinstance(result, dict)
        assert result["count"] == 50

        grades = [float(r["grade"]) for r in sample_csv_data]
        expected_mean = round(sum(grades) / len(grades), 2)
        assert abs(result["mean"] - expected_mean) < 0.02, (
            f"Expected mean ~{expected_mean}, got {result['mean']}"
        )
        assert abs(result["min"] - min(grades)) < 0.01
        assert abs(result["max"] - max(grades)) < 0.01

    def test_group_by_location_variant(
        self, samples_csv_path, variant_locations, sample_csv_data
    ):
        """group_by_location result should contain the variant locations."""
        from lab4_data_processor import group_by_location

        groups = group_by_location(samples_csv_path)
        for loc in variant_locations:
            assert loc in groups, f"Location {loc} should appear in groups"
            expected = [r["sample_id"] for r in sample_csv_data if r["location"] == loc]
            assert len(groups[loc]) == len(expected)

    def test_find_high_grade_samples_threshold(
        self, samples_csv_path, sample_csv_data
    ):
        """find_high_grade_samples should return correct count above threshold."""
        from lab4_data_processor import find_high_grade_samples

        threshold = 3.5
        expected = [r for r in sample_csv_data if float(r["grade"]) > threshold]
        result = find_high_grade_samples(samples_csv_path, threshold)
        assert len(result) == len(expected), (
            f"Expected {len(expected)} samples > {threshold}, got {len(result)}"
        )
        # Should be sorted descending by grade
        if len(result) >= 2:
            assert float(result[0]["grade"]) >= float(result[1]["grade"])

    def test_count_by_rock_type_correctness(self, samples_csv_path, sample_csv_data):
        """count_by_rock_type should match manual counts from the CSV."""
        from lab4_data_processor import count_by_rock_type

        result = count_by_rock_type(samples_csv_path)
        expected = {}
        for r in sample_csv_data:
            rt = r["rock_type"]
            expected[rt] = expected.get(rt, 0) + 1
        assert result == expected

    def test_calculate_average_by_group_location(
        self, samples_csv_path, sample_csv_data
    ):
        """calculate_average_by_group for location/grade should be correct."""
        from lab4_data_processor import calculate_average_by_group

        result = calculate_average_by_group(samples_csv_path, "location", "grade")
        # Compute expected
        sums = {}
        counts = {}
        for r in sample_csv_data:
            loc = r["location"]
            g = float(r["grade"])
            sums[loc] = sums.get(loc, 0) + g
            counts[loc] = counts.get(loc, 0) + 1
        for loc in sums:
            expected_avg = round(sums[loc] / counts[loc], 2)
            assert abs(result[loc] - expected_avg) < 0.02, (
                f"Average for {loc}: expected {expected_avg}, got {result[loc]}"
            )

    def test_find_depth_range_samples_variant(
        self, samples_csv_path, variant_depth_range, sample_csv_data
    ):
        """find_depth_range_samples with variant depth_range should match."""
        from lab4_data_processor import find_depth_range_samples

        min_d = variant_depth_range["min"]
        max_d = variant_depth_range["max"]
        expected = [
            r for r in sample_csv_data
            if min_d <= float(r["depth"]) <= max_d
        ]
        result = find_depth_range_samples(samples_csv_path, min_d, max_d)
        assert len(result) == len(expected), (
            f"Expected {len(expected)} samples in depth [{min_d}, {max_d}], "
            f"got {len(result)}"
        )


# ========================================================================
# TestHiddenErrorHandling  (~5 tests)
# ========================================================================


class TestHiddenErrorHandling:
    """Hidden tests for lab4_error_handling.py functions."""

    def test_safe_read_file_existing_and_missing(self, temp_dir):
        """safe_read_file should return (True, content) or (False, msg)."""
        from lab4_error_handling import safe_read_file

        # Existing file
        path = str(temp_dir / "exists.txt")
        with open(path, "w") as f:
            f.write("hidden test content")
        success, content = safe_read_file(path)
        assert success is True
        assert "hidden test content" in content

        # Missing file
        success, msg = safe_read_file(str(temp_dir / "no_such_file.txt"))
        assert success is False
        assert isinstance(msg, str)

    def test_safe_read_csv_actual_data(self, samples_csv_path):
        """safe_read_csv on the real CSV should succeed with 50 rows."""
        from lab4_error_handling import safe_read_csv

        success, data = safe_read_csv(samples_csv_path)
        assert success is True
        assert isinstance(data, list)
        assert len(data) == 50

    def test_validate_csv_row_valid_and_invalid(self):
        """validate_csv_row should correctly classify valid and invalid rows."""
        from lab4_error_handling import validate_csv_row

        valid_row = {
            "sample_id": "GEO-001",
            "rock_type": "Granite",
            "grade": "2.5",
            "depth": "150",
        }
        is_valid, errors = validate_csv_row(
            valid_row,
            required_fields=["sample_id", "rock_type"],
            numeric_fields=["grade", "depth"],
        )
        assert is_valid is True
        assert len(errors) == 0

        # Missing required field
        bad_row = {"sample_id": "", "rock_type": "Basalt", "grade": "1.0", "depth": "100"}
        is_valid, errors = validate_csv_row(
            bad_row,
            required_fields=["sample_id"],
            numeric_fields=["grade"],
        )
        assert is_valid is False
        assert len(errors) > 0

        # Invalid numeric
        bad_numeric = {"sample_id": "GEO-X", "grade": "N/A", "depth": "abc"}
        is_valid, errors = validate_csv_row(
            bad_numeric,
            required_fields=["sample_id"],
            numeric_fields=["grade", "depth"],
        )
        assert is_valid is False
        assert len(errors) >= 2

    def test_safe_convert_numeric_various(self):
        """safe_convert_numeric should handle a range of inputs."""
        from lab4_error_handling import safe_convert_numeric

        assert safe_convert_numeric("3.14") == pytest.approx(3.14)
        assert safe_convert_numeric("-7") == pytest.approx(-7.0)
        assert safe_convert_numeric("", default=-1) == -1
        assert safe_convert_numeric("abc") is None
        assert safe_convert_numeric("1e2") == pytest.approx(100.0)

    def test_process_csv_with_validation_actual(self, samples_csv_path):
        """process_csv_with_validation on real CSV should return structured result."""
        from lab4_error_handling import process_csv_with_validation

        result = process_csv_with_validation(samples_csv_path)
        assert isinstance(result, dict)
        assert "valid_rows" in result
        assert "invalid_rows" in result
        assert "error_count" in result
        total = len(result["valid_rows"]) + result["error_count"]
        assert total == 50, f"valid + invalid should equal 50, got {total}"


# ========================================================================
# TestHiddenVariantVerification  (~4 tests)
# ========================================================================


class TestHiddenVariantVerification:
    """Verify that the variant configuration is well-formed."""

    def test_variant_has_required_keys(self, variant_params):
        """Variant params should contain all required keys."""
        for key in ("num_records", "locations", "depth_range", "include_errors"):
            assert key in variant_params, f"Missing variant key: {key}"

    def test_variant_locations_exist_in_csv(self, variant_locations, sample_csv_data):
        """All variant locations should exist in the CSV data."""
        csv_locations = {r["location"] for r in sample_csv_data}
        for loc in variant_locations:
            assert loc in csv_locations, (
                f"Variant location '{loc}' not found in CSV. "
                f"CSV has: {csv_locations}"
            )

    def test_variant_depth_range_valid(self, variant_depth_range):
        """depth_range min should be less than max."""
        assert variant_depth_range["min"] < variant_depth_range["max"], (
            f"depth_range min ({variant_depth_range['min']}) should be < "
            f"max ({variant_depth_range['max']})"
        )

    def test_variant_num_records_in_range(self, variant_num_records):
        """num_records should be in the expected 40-60 range."""
        assert 40 <= variant_num_records <= 60, (
            f"num_records {variant_num_records} outside expected range [40, 60]"
        )


# ========================================================================
# TestHiddenIntegration  (~3 tests)
# ========================================================================


class TestHiddenIntegration:
    """Integration tests that combine multiple modules."""

    def test_read_process_stats_pipeline(self, samples_csv_path, sample_csv_data):
        """Read CSV -> calculate stats -> verify pipeline consistency."""
        from lab4_csv_reader import get_row_count, get_column_values
        from lab4_data_processor import calculate_statistics

        row_count = get_row_count(samples_csv_path)
        assert row_count == 50

        grades_str = get_column_values(samples_csv_path, "grade")
        assert len(grades_str) == 50

        stats = calculate_statistics(samples_csv_path, "grade")
        assert stats["count"] == 50

        grades_float = [float(g) for g in grades_str]
        assert abs(stats["min"] - min(grades_float)) < 0.01
        assert abs(stats["max"] - max(grades_float)) < 0.01

    def test_read_filter_write_roundtrip(self, samples_csv_path, temp_dir):
        """Read CSV -> filter -> write -> read back -> verify round-trip."""
        from lab4_csv_reader import read_samples_as_dict, get_row_count
        from lab4_csv_writer import filter_and_save

        output = str(temp_dir / "integration_filtered.csv")
        threshold = 3.0
        count = filter_and_save(samples_csv_path, output, "grade", threshold)
        assert count > 0

        # Read back and verify every row meets the threshold
        filtered = read_samples_as_dict(output)
        assert len(filtered) == count
        for row in filtered:
            assert float(row["grade"]) >= threshold

    def test_full_pipeline_with_error_handling(self, samples_csv_path, temp_dir):
        """Full pipeline: safe_read -> process -> write report -> verify."""
        from lab4_error_handling import safe_read_csv, check_file_exists
        from lab4_data_processor import (
            calculate_statistics,
            generate_summary_report,
        )

        # Step 1: safely read
        success, data = safe_read_csv(samples_csv_path)
        assert success is True
        assert len(data) == 50

        # Step 2: calculate statistics
        stats = calculate_statistics(samples_csv_path, "grade")
        assert stats["count"] == 50
        assert stats["min"] <= stats["mean"] <= stats["max"]

        # Step 3: generate report
        report_path = str(temp_dir / "integration_report.txt")
        generate_summary_report(samples_csv_path, report_path)
        assert check_file_exists(report_path)

        with open(report_path) as f:
            content = f.read()
        assert len(content) > 50, "Report should contain meaningful content"
