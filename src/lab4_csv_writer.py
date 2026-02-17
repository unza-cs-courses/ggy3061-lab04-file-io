# lab4_csv_writer.py
"""
Lab 4 Task 3: Writing CSV Files
Learn to create and write CSV files using the csv module.

Learning Outcomes:
- LO4.2: Process CSV files using the csv module
- LO4.4: Use context managers (with statement) for file operations
"""

import csv


def write_samples_from_list(filepath: str, header: list, rows: list) -> int:
    """
    Write data to a CSV file from lists.

    Args:
        filepath: Path to the output CSV file
        header: List of column names
        rows: List of lists (data rows)

    Returns:
        Number of data rows written (excluding header)

    Example:
        header = ['sample_id', 'rock_type', 'grade']
        rows = [
            ['GEO-001', 'Granite', '2.5'],
            ['GEO-002', 'Basalt', '1.8']
        ]
        count = write_samples_from_list('output.csv', header, rows)
        # Returns 2
    """
    # TODO: Implement this function
    # Use 'with' statement to open file with newline=''
    # Create csv.writer object
    # Write header row using writerow()
    # Write data rows using writerows() or writerow() in a loop
    # Return count of data rows written
    pass


def write_samples_from_dict(filepath: str, fieldnames: list, rows: list) -> int:
    """
    Write data to a CSV file from dictionaries.

    Args:
        filepath: Path to the output CSV file
        fieldnames: List of column names (determines column order)
        rows: List of dictionaries (data rows)

    Returns:
        Number of data rows written

    Example:
        fieldnames = ['sample_id', 'rock_type', 'grade']
        rows = [
            {'sample_id': 'GEO-001', 'rock_type': 'Granite', 'grade': '2.5'},
            {'sample_id': 'GEO-002', 'rock_type': 'Basalt', 'grade': '1.8'}
        ]
        count = write_samples_from_dict('output.csv', fieldnames, rows)
        # Returns 2
    """
    # TODO: Implement this function
    # Use 'with' statement to open file with newline=''
    # Create csv.DictWriter object with fieldnames
    # Write header using writeheader()
    # Write data rows using writerows() or writerow() in a loop
    # Return count of data rows written
    pass


def filter_and_save(input_path: str, output_path: str,
                    column: str, min_value: float) -> int:
    """
    Read CSV, filter rows by numeric column, and save filtered data.

    Args:
        input_path: Path to input CSV file
        output_path: Path to output CSV file
        column: Name of the numeric column to filter
        min_value: Minimum value (inclusive) to include

    Returns:
        Number of rows in the filtered output

    Example:
        # Filter samples with grade >= 2.0
        count = filter_and_save('input.csv', 'output.csv', 'grade', 2.0)
    """
    # TODO: Implement this function
    # Read input CSV using DictReader
    # Filter rows where float(row[column]) >= min_value
    # Handle conversion errors (skip rows that can't be converted)
    # Write filtered rows to output CSV using DictWriter
    # Return count of filtered rows
    pass


def append_row_to_csv(filepath: str, row: dict) -> bool:
    """
    Append a single row to an existing CSV file.

    Args:
        filepath: Path to the existing CSV file
        row: Dictionary representing the row to append

    Returns:
        True if successful, False otherwise

    Example:
        new_sample = {'sample_id': 'GEO-051', 'rock_type': 'Granite', 'grade': '3.1'}
        success = append_row_to_csv('data/samples.csv', new_sample)
    """
    # TODO: Implement this function
    # First, read the existing headers from the file
    # Open file in append mode ('a') with newline=''
    # Create DictWriter with existing headers
    # Write the new row
    # Return True if successful
    pass


def merge_csv_files(file_paths: list, output_path: str) -> int:
    """
    Merge multiple CSV files with the same structure into one.

    Args:
        file_paths: List of paths to CSV files to merge
        output_path: Path to the output merged CSV file

    Returns:
        Total number of data rows in merged file

    Example:
        files = ['data1.csv', 'data2.csv', 'data3.csv']
        total = merge_csv_files(files, 'merged.csv')
    """
    # TODO: Implement this function
    # Read headers from first file
    # Open output file and write headers
    # Read each input file and write its data rows
    # Return total count of data rows
    pass


def create_sample_csv(filepath: str, num_samples: int) -> int:
    """
    Create a CSV file with sample geological data.

    Args:
        filepath: Path to create the CSV file
        num_samples: Number of sample rows to generate

    Returns:
        Number of rows created

    Example:
        count = create_sample_csv('new_samples.csv', 10)
    """
    # TODO: Implement this function
    # Define headers: ['sample_id', 'rock_type', 'grade', 'depth', 'location']
    # Generate sample data for each row
    # Use sample IDs like 'GEO-001', 'GEO-002', etc.
    # Write to CSV file
    # Return number of rows created
    pass


# =============================================================================
# Test your code by running this file directly
# =============================================================================

if __name__ == "__main__":
    import os

    print("Testing CSV writer functions\n")

    # Test data
    test_header = ['sample_id', 'rock_type', 'grade']
    test_rows_list = [
        ['GEO-001', 'Granite', '2.5'],
        ['GEO-002', 'Basalt', '1.8'],
        ['GEO-003', 'Sandstone', '3.2']
    ]
    test_rows_dict = [
        {'sample_id': 'GEO-001', 'rock_type': 'Granite', 'grade': '2.5'},
        {'sample_id': 'GEO-002', 'rock_type': 'Basalt', 'grade': '1.8'},
        {'sample_id': 'GEO-003', 'rock_type': 'Sandstone', 'grade': '3.2'}
    ]

    # Uncomment to test your implementation:
    # count = write_samples_from_list('test_output_list.csv', test_header, test_rows_list)
    # print(f"Wrote {count} rows to test_output_list.csv")

    # count = write_samples_from_dict('test_output_dict.csv', test_header, test_rows_dict)
    # print(f"Wrote {count} rows to test_output_dict.csv")

    print("Uncomment the test code above to test your implementation.")
