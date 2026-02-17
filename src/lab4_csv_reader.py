# lab4_csv_reader.py
"""
Lab 4 Task 2: Reading CSV Files
Learn to read and parse CSV files using the csv module.

Learning Outcomes:
- LO4.2: Process CSV files using the csv module
- LO4.4: Use context managers (with statement) for file operations
"""

import csv


def read_samples_as_list(filepath: str) -> list:
    """
    Read CSV file and return data as list of lists.

    Args:
        filepath: Path to the CSV file

    Returns:
        List of lists (each inner list is a row, including header)

    Example:
        data = read_samples_as_list('data/samples.csv')
        header = data[0]  # ['sample_id', 'rock_type', 'grade', ...]
        first_row = data[1]  # ['GEO-001', 'Granite', '2.5', ...]
    """
    # TODO: Implement this function
    # Use 'with' statement to open the file
    # Create csv.reader object
    # Convert to list and return
    # Remember to use newline='' when opening CSV files
    pass


def read_samples_as_dict(filepath: str) -> list:
    """
    Read CSV file and return data as list of dictionaries.

    Args:
        filepath: Path to the CSV file

    Returns:
        List of dictionaries (each dict is a row with column names as keys)

    Example:
        samples = read_samples_as_dict('data/samples.csv')
        # [{'sample_id': 'GEO-001', 'rock_type': 'Granite', 'grade': '2.5'}, ...]
        print(samples[0]['sample_id'])  # 'GEO-001'
    """
    # TODO: Implement this function
    # Use 'with' statement to open the file with newline=''
    # Use csv.DictReader to read the CSV file
    # Convert to list and return
    pass


def get_column_values(filepath: str, column_name: str) -> list:
    """
    Extract all values from a specific column.

    Args:
        filepath: Path to the CSV file
        column_name: Name of the column to extract

    Returns:
        List of values from that column (as strings)

    Example:
        grades = get_column_values('data/samples.csv', 'grade')
        # ['2.5', '1.8', '3.2', ...]
    """
    # TODO: Implement this function
    # Use csv.DictReader to read the file
    # Extract values from the specified column
    # Return as a list
    pass


def get_unique_values(filepath: str, column_name: str) -> set:
    """
    Get unique values from a specific column.

    Args:
        filepath: Path to the CSV file
        column_name: Name of the column

    Returns:
        Set of unique values from that column

    Example:
        rock_types = get_unique_values('data/samples.csv', 'rock_type')
        # {'Granite', 'Basalt', 'Sandstone'}
    """
    # TODO: Implement this function
    # Use get_column_values to get all values
    # Convert to set to remove duplicates
    pass


def get_row_count(filepath: str) -> int:
    """
    Count the number of data rows in a CSV file (excluding header).

    Args:
        filepath: Path to the CSV file

    Returns:
        Number of data rows

    Example:
        count = get_row_count('data/samples.csv')
        # 50
    """
    # TODO: Implement this function
    # Read CSV and count rows (excluding header)
    pass


def find_rows_by_value(filepath: str, column_name: str, value: str) -> list:
    """
    Find all rows where a column matches a specific value.

    Args:
        filepath: Path to the CSV file
        column_name: Name of the column to search
        value: Value to match

    Returns:
        List of dictionaries for matching rows

    Example:
        granite_samples = find_rows_by_value('data/samples.csv', 'rock_type', 'Granite')
        # [{'sample_id': 'GEO-001', 'rock_type': 'Granite', ...}, ...]
    """
    # TODO: Implement this function
    # Read CSV using DictReader
    # Filter rows where column_name == value
    # Return list of matching row dictionaries
    pass


def get_csv_headers(filepath: str) -> list:
    """
    Get the column headers from a CSV file.

    Args:
        filepath: Path to the CSV file

    Returns:
        List of column header names

    Example:
        headers = get_csv_headers('data/samples.csv')
        # ['sample_id', 'rock_type', 'grade', 'depth', 'mass', 'location']
    """
    # TODO: Implement this function
    # Read only the first row of the CSV
    # Return as a list
    pass


# =============================================================================
# Test your code by running this file directly
# =============================================================================

if __name__ == "__main__":
    import os

    # Find the data file relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, '..', 'data', 'samples.csv')

    if os.path.exists(data_path):
        print(f"Testing with: {data_path}\n")

        # Uncomment to test your implementation:
        # print("Headers:", get_csv_headers(data_path))
        # print(f"\nRow count: {get_row_count(data_path)}")
        # print(f"\nUnique rock types: {get_unique_values(data_path, 'rock_type')}")
        # print(f"\nUnique locations: {get_unique_values(data_path, 'location')}")

        print("Uncomment the test code above to test your implementation.")
    else:
        print(f"Data file not found: {data_path}")
        print("Run this file from the repository root directory.")
