"""
Lab 4 Visible Tests - File I/O & CSV Processing
Comprehensive functional tests that verify correct implementation.
Starter templates (returning None/pass) will NOT pass these tests.
"""

import subprocess
import sys
import os
import csv
import tempfile
from pathlib import Path

import pytest

SRC_DIR = Path(__file__).parent.parent.parent / "src"
DATA_DIR = Path(__file__).parent.parent.parent / "data"

# Add src to path so we can import student modules
sys.path.insert(0, str(SRC_DIR))


def run_script(script_name, input_data=None):
    """Run a Python script and capture output."""
    script_path = SRC_DIR / script_name
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        input=input_data,
        timeout=30,
    )
    return result


# ========================================================================
# Fixtures
# ========================================================================

@pytest.fixture
def samples_csv_path():
    """Path to the provided samples.csv data file."""
    return str(DATA_DIR / "samples.csv")


@pytest.fixture
def tmp_dir(tmp_path):
    """Provide a temporary directory for file output tests."""
    return tmp_path


@pytest.fixture
def sample_log_data():
    """Sample data for text I/O tests."""
    return [
        {"id": "GEO-001", "rock_type": "Granite", "grade": 2.5},
        {"id": "GEO-002", "rock_type": "Basalt", "grade": 1.8},
        {"id": "GEO-003", "rock_type": "Sandstone", "grade": 3.2},
    ]


@pytest.fixture
def small_csv(tmp_path):
    """Create a small CSV file for testing."""
    csv_path = tmp_path / "test_samples.csv"
    rows = [
        ["sample_id", "rock_type", "grade", "depth", "mass", "location"],
        ["GEO-001", "Granite", "2.5", "150", "12.3", "Site-A"],
        ["GEO-002", "Basalt", "3.2", "200", "15.1", "Site-A"],
        ["GEO-003", "Granite", "1.8", "180", "11.8", "Site-B"],
        ["GEO-004", "Schist", "4.1", "250", "14.5", "Site-B"],
    ]
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return str(csv_path)


# ========================================================================
# Task 1: Text File I/O
# ========================================================================


class TestTask1TextIO:
    """Tests for basic text file I/O functions."""

    def test_text_io_file_exists(self):
        """lab4_text_io.py should exist."""
        assert (SRC_DIR / "lab4_text_io.py").exists()

    def test_write_sample_log_returns_int(self, tmp_dir, sample_log_data):
        """write_sample_log should return the number of lines written."""
        from lab4_text_io import write_sample_log

        output_path = str(tmp_dir / "test_log.txt")
        result = write_sample_log(output_path, sample_log_data)
        assert isinstance(result, int), "write_sample_log must return an integer"
        assert result > 0, "write_sample_log must return a positive count"

    def test_write_sample_log_creates_file(self, tmp_dir, sample_log_data):
        """write_sample_log should create the output file."""
        from lab4_text_io import write_sample_log

        output_path = str(tmp_dir / "test_log.txt")
        write_sample_log(output_path, sample_log_data)
        assert os.path.exists(output_path), "Log file should be created"

    def test_write_sample_log_content(self, tmp_dir, sample_log_data):
        """write_sample_log should write correct content."""
        from lab4_text_io import write_sample_log

        output_path = str(tmp_dir / "test_log.txt")
        write_sample_log(output_path, sample_log_data)
        with open(output_path) as f:
            content = f.read()
        assert "GEO-001" in content, "Log should contain sample IDs"
        assert "Granite" in content, "Log should contain rock types"

    def test_read_sample_log_returns_list(self, tmp_dir, sample_log_data):
        """read_sample_log should return a list."""
        from lab4_text_io import write_sample_log, read_sample_log

        output_path = str(tmp_dir / "test_log.txt")
        write_sample_log(output_path, sample_log_data)
        result = read_sample_log(output_path)
        assert isinstance(result, list), "read_sample_log must return a list"

    def test_count_lines_returns_int(self, tmp_dir, sample_log_data):
        """count_lines should return an integer."""
        from lab4_text_io import write_sample_log, count_lines

        output_path = str(tmp_dir / "test_log.txt")
        write_sample_log(output_path, sample_log_data)
        result = count_lines(output_path)
        assert isinstance(result, int), "count_lines must return an integer"
        assert result > 0, "count_lines must return a positive count"

    def test_write_lines_returns_count(self, tmp_dir):
        """write_lines should return the number of lines written."""
        from lab4_text_io import write_lines

        output_path = str(tmp_dir / "test_lines.txt")
        result = write_lines(output_path, ["A", "B", "C"])
        assert result == 3, "write_lines should return 3 for 3 lines"

    def test_append_to_log_adds_content(self, tmp_dir, sample_log_data):
        """append_to_log should add a message to an existing file."""
        from lab4_text_io import write_sample_log, append_to_log

        output_path = str(tmp_dir / "test_log.txt")
        write_sample_log(output_path, sample_log_data)
        append_to_log(output_path, "--- End of Log ---")
        with open(output_path) as f:
            content = f.read()
        assert "End of Log" in content, "Appended message should appear in file"

    def test_read_file_content_returns_string(self, tmp_dir, sample_log_data):
        """read_file_content should return the entire file as a string."""
        from lab4_text_io import write_sample_log, read_file_content

        output_path = str(tmp_dir / "test_log.txt")
        write_sample_log(output_path, sample_log_data)
        result = read_file_content(output_path)
        assert isinstance(result, str), "read_file_content must return a string"
        assert "GEO-001" in result, "Content should include sample IDs"


# ========================================================================
# Task 2: CSV Reader
# ========================================================================


class TestTask2CSVReader:
    """Tests for CSV reading functions."""

    def test_csv_reader_file_exists(self):
        """lab4_csv_reader.py should exist."""
        assert (SRC_DIR / "lab4_csv_reader.py").exists()

    def test_read_samples_as_list_returns_list(self, small_csv):
        """read_samples_as_list should return a list."""
        from lab4_csv_reader import read_samples_as_list

        result = read_samples_as_list(small_csv)
        assert isinstance(result, list), "Must return a list"
        assert len(result) > 0, "Must return non-empty list"

    def test_read_samples_as_list_includes_header(self, small_csv):
        """read_samples_as_list should include the header row."""
        from lab4_csv_reader import read_samples_as_list

        result = read_samples_as_list(small_csv)
        assert result[0][0] == "sample_id", \
            "First element of header should be 'sample_id'"

    def test_read_samples_as_list_row_count(self, small_csv):
        """read_samples_as_list should return all rows (header + data)."""
        from lab4_csv_reader import read_samples_as_list

        result = read_samples_as_list(small_csv)
        assert len(result) == 5, "Should have 1 header + 4 data rows = 5"

    def test_read_samples_as_dict_returns_list(self, small_csv):
        """read_samples_as_dict should return a list of dictionaries."""
        from lab4_csv_reader import read_samples_as_dict

        result = read_samples_as_dict(small_csv)
        assert isinstance(result, list), "Must return a list"
        assert len(result) == 4, "Should have 4 data rows"
        assert isinstance(result[0], dict), "Each row should be a dictionary"

    def test_read_samples_as_dict_keys(self, small_csv):
        """read_samples_as_dict rows should have correct keys."""
        from lab4_csv_reader import read_samples_as_dict

        result = read_samples_as_dict(small_csv)
        expected_keys = {
            "sample_id", "rock_type", "grade", "depth", "mass", "location"
        }
        assert set(result[0].keys()) == expected_keys

    def test_get_column_values_returns_list(self, small_csv):
        """get_column_values should return a list of values."""
        from lab4_csv_reader import get_column_values

        result = get_column_values(small_csv, "rock_type")
        assert isinstance(result, list), "Must return a list"
        assert len(result) == 4, "Should have 4 values"

    def test_get_column_values_correct(self, small_csv):
        """get_column_values should return correct values."""
        from lab4_csv_reader import get_column_values

        result = get_column_values(small_csv, "sample_id")
        assert "GEO-001" in result, "Should contain GEO-001"
        assert "GEO-004" in result, "Should contain GEO-004"

    def test_get_unique_values_returns_set(self, small_csv):
        """get_unique_values should return a set."""
        from lab4_csv_reader import get_unique_values

        result = get_unique_values(small_csv, "rock_type")
        assert isinstance(result, set), "Must return a set"
        assert "Granite" in result
        assert len(result) == 3, "Should have 3 unique rock types"

    def test_get_row_count(self, small_csv):
        """get_row_count should return number of data rows."""
        from lab4_csv_reader import get_row_count

        result = get_row_count(small_csv)
        assert result == 4, f"Expected 4 data rows, got {result}"

    def test_find_rows_by_value_returns_matches(self, small_csv):
        """find_rows_by_value should return matching rows."""
        from lab4_csv_reader import find_rows_by_value

        result = find_rows_by_value(small_csv, "rock_type", "Granite")
        assert isinstance(result, list), "Must return a list"
        assert len(result) == 2, "Should find 2 Granite rows"

    def test_get_csv_headers(self, small_csv):
        """get_csv_headers should return column names."""
        from lab4_csv_reader import get_csv_headers

        result = get_csv_headers(small_csv)
        assert isinstance(result, list), "Must return a list"
        assert "sample_id" in result, "Should contain 'sample_id'"
        assert len(result) == 6, "Should have 6 columns"

    def test_with_real_data_file(self, samples_csv_path):
        """CSV reader functions should work with the real samples.csv."""
        from lab4_csv_reader import get_row_count

        result = get_row_count(samples_csv_path)
        assert result == 50, f"samples.csv should have 50 rows, got {result}"


# ========================================================================
# Task 3: CSV Writer
# ========================================================================


class TestTask3CSVWriter:
    """Tests for CSV writing functions."""

    def test_csv_writer_file_exists(self):
        """lab4_csv_writer.py should exist."""
        assert (SRC_DIR / "lab4_csv_writer.py").exists()

    def test_write_samples_from_list(self, tmp_dir):
        """write_samples_from_list should create a valid CSV file."""
        from lab4_csv_writer import write_samples_from_list

        output_path = str(tmp_dir / "output.csv")
        header = ["sample_id", "rock_type", "grade"]
        data = [
            ["GEO-001", "Granite", "2.5"],
            ["GEO-002", "Basalt", "3.2"],
        ]
        result = write_samples_from_list(output_path, header, data)
        assert os.path.exists(output_path), "CSV file should be created"
        with open(output_path, newline="") as f:
            reader = csv.reader(f)
            rows = list(reader)
        assert len(rows) == 3, "Should have 1 header + 2 data rows"
        assert rows[0] == header

    def test_write_samples_from_dict(self, tmp_dir):
        """write_samples_from_dict should create a valid CSV file."""
        from lab4_csv_writer import write_samples_from_dict

        output_path = str(tmp_dir / "output.csv")
        data = [
            {"sample_id": "GEO-001", "rock_type": "Granite", "grade": "2.5"},
            {"sample_id": "GEO-002", "rock_type": "Basalt", "grade": "3.2"},
        ]
        fieldnames = ["sample_id", "rock_type", "grade"]
        write_samples_from_dict(output_path, data, fieldnames)
        assert os.path.exists(output_path), "CSV file should be created"
        with open(output_path, newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        assert len(rows) == 2, "Should have 2 data rows"

    def test_filter_and_save(self, small_csv, tmp_dir):
        """filter_and_save should write filtered rows to new CSV."""
        from lab4_csv_writer import filter_and_save

        output_path = str(tmp_dir / "filtered.csv")
        # small_csv grades: 2.5, 3.2, 1.8, 4.1 — two are >= 3.0
        result = filter_and_save(small_csv, output_path, "grade", 3.0)
        assert os.path.exists(output_path), "Filtered CSV should be created"
        with open(output_path, newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        assert len(rows) == 2, "Should have 2 rows with grade >= 3.0"

    def test_append_row_to_csv(self, small_csv):
        """append_row_to_csv should add a row to an existing CSV file."""
        from lab4_csv_writer import append_row_to_csv

        new_row = {
            "sample_id": "GEO-099", "rock_type": "Marble",
            "grade": "5.0", "depth": "100", "mass": "10.0", "location": "Site-C"
        }
        result = append_row_to_csv(small_csv, new_row)
        assert result is True, "append_row_to_csv should return True on success"
        with open(small_csv, newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        assert len(rows) == 5, "Should have 5 rows after appending"

    def test_merge_csv_files(self, tmp_dir):
        """merge_csv_files should merge multiple CSV files into one."""
        from lab4_csv_writer import merge_csv_files

        # Create two small CSV files
        file1 = str(tmp_dir / "f1.csv")
        file2 = str(tmp_dir / "f2.csv")
        for path, ids in [(file1, ["GEO-001"]), (file2, ["GEO-002", "GEO-003"])]:
            with open(path, "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["sample_id", "grade"])
                for sid in ids:
                    w.writerow([sid, "2.0"])
        output_path = str(tmp_dir / "merged.csv")
        result = merge_csv_files([file1, file2], output_path)
        assert isinstance(result, int), "merge_csv_files must return an integer"
        assert result == 3, "Should have 3 merged data rows"

    def test_create_sample_csv(self, tmp_dir):
        """create_sample_csv should create a CSV with generated data."""
        from lab4_csv_writer import create_sample_csv

        output_path = str(tmp_dir / "generated.csv")
        result = create_sample_csv(output_path, 5)
        assert isinstance(result, int), "create_sample_csv must return an integer"
        assert result == 5, "Should create 5 rows"
        assert os.path.exists(output_path), "CSV file should be created"


# ========================================================================
# Task 4: Data Processor
# ========================================================================


class TestTask4DataProcessor:
    """Tests for data processing functions."""

    def test_data_processor_file_exists(self):
        """lab4_data_processor.py should exist."""
        assert (SRC_DIR / "lab4_data_processor.py").exists()

    def test_calculate_statistics_returns_dict(self, small_csv):
        """calculate_statistics should return a dictionary with stats."""
        from lab4_data_processor import calculate_statistics

        result = calculate_statistics(small_csv, "grade")
        assert isinstance(result, dict), "Must return a dictionary"
        assert "mean" in result or "average" in result or "avg" in result, \
            "Result should contain a mean/average key"

    def test_calculate_statistics_values(self, small_csv):
        """calculate_statistics should compute correct values."""
        from lab4_data_processor import calculate_statistics

        result = calculate_statistics(small_csv, "grade")
        mean_key = next(
            (k for k in result if k in ("mean", "average", "avg")), None
        )
        assert mean_key is not None, "Should have a mean/average key"
        assert abs(result[mean_key] - 2.9) < 0.1, \
            f"Mean of grades should be ~2.9, got {result[mean_key]}"

    def test_find_high_grade_samples(self, small_csv):
        """find_high_grade_samples should return samples above threshold."""
        from lab4_data_processor import find_high_grade_samples

        result = find_high_grade_samples(small_csv, 3.0)
        assert isinstance(result, list), "Must return a list"
        assert len(result) == 2, "Should find 2 samples with grade >= 3.0"

    def test_group_by_location(self, small_csv):
        """group_by_location should group samples by their location."""
        from lab4_data_processor import group_by_location

        result = group_by_location(small_csv)
        assert isinstance(result, dict), "Must return a dictionary"
        assert "Site-A" in result, "Should have Site-A group"
        assert "Site-B" in result, "Should have Site-B group"
        assert len(result["Site-A"]) == 2, "Site-A should have 2 samples"

    def test_count_by_rock_type_returns_dict(self, small_csv):
        """count_by_rock_type should return a dictionary of counts."""
        from lab4_data_processor import count_by_rock_type

        result = count_by_rock_type(small_csv)
        assert isinstance(result, dict), "Must return a dictionary"
        assert result.get("Granite") == 2, "Should have 2 Granite samples"

    def test_calculate_average_by_group(self, small_csv):
        """calculate_average_by_group should return grouped averages."""
        from lab4_data_processor import calculate_average_by_group

        result = calculate_average_by_group(small_csv, "location", "grade")
        assert isinstance(result, dict), "Must return a dictionary"
        assert "Site-A" in result, "Should have Site-A average"
        assert isinstance(result["Site-A"], (int, float)), "Average should be numeric"

    def test_generate_summary_report_creates_file(self, small_csv, tmp_dir):
        """generate_summary_report should create a text report file."""
        from lab4_data_processor import generate_summary_report

        output_path = str(tmp_dir / "report.txt")
        generate_summary_report(small_csv, output_path)
        assert os.path.exists(output_path), "Report file should be created"
        with open(output_path) as f:
            content = f.read()
        assert len(content) > 0, "Report should not be empty"

    def test_find_depth_range_samples(self, small_csv):
        """find_depth_range_samples should return samples in depth range."""
        from lab4_data_processor import find_depth_range_samples

        # small_csv depths: 150, 200, 180, 250 — three in 150-200 range
        result = find_depth_range_samples(small_csv, 150, 200)
        assert isinstance(result, list), "Must return a list"
        assert len(result) == 3, "Should find 3 samples with depth 150-200"


# ========================================================================
# Task 5: Error Handling
# ========================================================================


class TestTask5ErrorHandling:
    """Tests for error handling functions."""

    def test_error_handling_file_exists(self):
        """lab4_error_handling.py should exist."""
        assert (SRC_DIR / "lab4_error_handling.py").exists()

    def test_safe_read_file_existing(self, tmp_dir):
        """safe_read_file should successfully read an existing file."""
        from lab4_error_handling import safe_read_file

        test_path = str(tmp_dir / "test.txt")
        with open(test_path, "w") as f:
            f.write("Hello World")
        result = safe_read_file(test_path)
        assert isinstance(result, tuple), "Must return a tuple"
        assert len(result) == 2, "Tuple should have 2 elements"
        assert result[0] is True, "First element should be True for success"

    def test_safe_read_file_missing(self):
        """safe_read_file should handle missing files gracefully."""
        from lab4_error_handling import safe_read_file

        result = safe_read_file("/nonexistent/path/file.txt")
        assert isinstance(result, tuple), "Must return a tuple"
        assert result[0] is False, "First element should be False for error"

    def test_safe_read_csv_existing(self, small_csv):
        """safe_read_csv should successfully read an existing CSV file."""
        from lab4_error_handling import safe_read_csv

        result = safe_read_csv(small_csv)
        assert isinstance(result, tuple), "Must return a tuple"
        assert result[0] is True, "Should succeed on valid CSV"
        assert isinstance(result[1], list), "Data should be a list"
        assert len(result[1]) == 4, "Should have 4 rows"

    def test_safe_read_csv_missing(self):
        """safe_read_csv should handle missing CSV gracefully."""
        from lab4_error_handling import safe_read_csv

        result = safe_read_csv("/nonexistent/path/data.csv")
        assert isinstance(result, tuple), "Must return a tuple"
        assert result[0] is False, "Should fail on missing file"

    def test_validate_csv_row_valid(self):
        """validate_csv_row should accept valid rows."""
        from lab4_error_handling import validate_csv_row

        row = {"sample_id": "GEO-001", "grade": "2.5", "depth": "150"}
        result = validate_csv_row(
            row,
            required_fields=["sample_id"],
            numeric_fields=["grade", "depth"],
        )
        assert isinstance(result, tuple), "Must return a tuple"
        assert result[0] is True, "Valid row should pass validation"

    def test_validate_csv_row_missing_field(self):
        """validate_csv_row should detect missing required fields."""
        from lab4_error_handling import validate_csv_row

        row = {"sample_id": "", "grade": "2.5"}
        result = validate_csv_row(row, required_fields=["sample_id"])
        assert isinstance(result, tuple), "Must return a tuple"
        assert result[0] is False, "Empty required field should fail"

    def test_validate_csv_row_invalid_numeric(self):
        """validate_csv_row should detect non-numeric values."""
        from lab4_error_handling import validate_csv_row

        row = {"sample_id": "GEO-001", "grade": "invalid", "depth": "150"}
        result = validate_csv_row(
            row,
            required_fields=["sample_id"],
            numeric_fields=["grade"],
        )
        assert isinstance(result, tuple), "Must return a tuple"
        assert result[0] is False, "Non-numeric grade should fail"

    def test_safe_convert_numeric_valid(self):
        """safe_convert_numeric should convert valid numbers."""
        from lab4_error_handling import safe_convert_numeric

        assert safe_convert_numeric("2.5") == 2.5
        assert safe_convert_numeric("42") == 42.0

    def test_safe_convert_numeric_invalid(self):
        """safe_convert_numeric should return default for invalid input."""
        from lab4_error_handling import safe_convert_numeric

        assert safe_convert_numeric("N/A", default=0.0) == 0.0
        assert safe_convert_numeric("", default=None) is None

    def test_check_file_exists_true(self, small_csv):
        """check_file_exists should return True for existing file."""
        from lab4_error_handling import check_file_exists

        result = check_file_exists(small_csv)
        assert result is True

    def test_check_file_exists_false(self):
        """check_file_exists should return False for missing file."""
        from lab4_error_handling import check_file_exists

        result = check_file_exists("/nonexistent/file.csv")
        assert result is False

    def test_safe_write_file_creates_file(self, tmp_dir):
        """safe_write_file should write content and return success tuple."""
        from lab4_error_handling import safe_write_file

        output_path = str(tmp_dir / "safe_output.txt")
        result = safe_write_file(output_path, "Hello World")
        assert isinstance(result, tuple), "Must return a tuple"
        assert result[0] is True, "First element should be True on success"
        with open(output_path) as f:
            content = f.read()
        assert "Hello World" in content

    def test_process_csv_with_validation_returns_dict(self, small_csv):
        """process_csv_with_validation should return a summary dictionary."""
        from lab4_error_handling import process_csv_with_validation

        result = process_csv_with_validation(small_csv)
        assert isinstance(result, dict), "Must return a dictionary"
        assert "valid_rows" in result, "Should have 'valid_rows' key"
        assert "invalid_rows" in result, "Should have 'invalid_rows' key"
        assert "error_count" in result, "Should have 'error_count' key"

    def test_get_file_info_existing_file(self, small_csv):
        """get_file_info should return info dict for existing file."""
        from lab4_error_handling import get_file_info

        result = get_file_info(small_csv)
        assert isinstance(result, dict), "Must return a dictionary"
        assert result.get("exists") is True, "Should report file exists"

    def test_get_file_info_missing_file(self):
        """get_file_info should handle missing file."""
        from lab4_error_handling import get_file_info

        result = get_file_info("/nonexistent/file.txt")
        assert isinstance(result, dict), "Must return a dictionary"
        assert result.get("exists") is False, "Should report file does not exist"


# ========================================================================
# Data File Checks
# ========================================================================


class TestDataFiles:
    """Tests for required data files."""

    def test_samples_csv_exists(self):
        """samples.csv should exist in data directory."""
        assert (DATA_DIR / "samples.csv").exists()

    def test_samples_csv_has_correct_columns(self):
        """samples.csv should have the expected columns."""
        with open(DATA_DIR / "samples.csv", newline="") as f:
            reader = csv.reader(f)
            header = next(reader)
        expected = {
            "sample_id", "rock_type", "grade", "depth", "mass", "location"
        }
        assert set(header) == expected, \
            f"Expected columns {expected}, got {set(header)}"

    def test_samples_csv_has_50_rows(self):
        """samples.csv should have 50 data rows."""
        with open(DATA_DIR / "samples.csv", newline="") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            rows = list(reader)
        assert len(rows) == 50, f"Expected 50 rows, got {len(rows)}"
