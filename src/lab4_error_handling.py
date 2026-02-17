# lab4_error_handling.py
"""
Lab 4 Task 5: Error Handling for File Operations
Learn to handle file-related errors gracefully.

Learning Outcomes:
- LO4.3: Handle file-related errors gracefully with try/except
- LO4.4: Use context managers (with statement) for file operations
"""

import csv


def safe_read_file(filepath: str) -> tuple:
    """
    Safely read a file with proper error handling.

    Args:
        filepath: Path to the file to read

    Returns:
        Tuple of (success: bool, content_or_error: str)
        If successful: (True, file_content)
        If error: (False, error_message)

    Example:
        success, result = safe_read_file('existing.txt')
        if success:
            print(result)  # File content

        success, result = safe_read_file('missing.txt')
        if not success:
            print(f"Error: {result}")  # "File not found: missing.txt"
    """
    # TODO: Implement this function
    # Use try/except to handle errors:
    # - FileNotFoundError: return (False, "File not found: {filepath}")
    # - PermissionError: return (False, "Permission denied: {filepath}")
    # - Exception: return (False, "Error reading file: {str(e)}")
    # If successful: return (True, file_content)
    pass


def safe_read_csv(filepath: str) -> tuple:
    """
    Safely read a CSV file with error handling.

    Args:
        filepath: Path to the CSV file

    Returns:
        Tuple of (success: bool, data_or_error: list|str)
        If successful: (True, list_of_dicts)
        If error: (False, error_message)

    Example:
        success, result = safe_read_csv('data/samples.csv')
        if success:
            for row in result:
                print(row)
    """
    # TODO: Implement this function
    # Handle file errors and CSV parsing errors
    # Use csv.DictReader to read the file
    # Return (True, list_of_dicts) on success
    # Return (False, error_message) on failure
    pass


def safe_write_file(filepath: str, content: str) -> tuple:
    """
    Safely write to a file with error handling.

    Args:
        filepath: Path to write to
        content: Content to write

    Returns:
        Tuple of (success: bool, message: str)
        If successful: (True, "Successfully wrote to {filepath}")
        If error: (False, error_message)

    Example:
        success, message = safe_write_file('output.txt', 'Hello World')
        print(message)
    """
    # TODO: Implement this function
    # Handle PermissionError and other potential errors
    # Return appropriate tuple based on success/failure
    pass


def validate_csv_row(row: dict, required_fields: list,
                     numeric_fields: list = None) -> tuple:
    """
    Validate a CSV row has required fields and valid numeric values.

    Args:
        row: Dictionary representing a CSV row
        required_fields: List of field names that must be present and non-empty
        numeric_fields: List of field names that must be numeric (optional)

    Returns:
        Tuple of (is_valid: bool, errors: list)
        errors is a list of error message strings

    Example:
        row = {'sample_id': 'GEO-001', 'grade': '2.5', 'depth': 'invalid'}
        valid, errors = validate_csv_row(
            row,
            required_fields=['sample_id', 'grade'],
            numeric_fields=['grade', 'depth']
        )
        # Returns: (False, ["Field 'depth' is not a valid number"])

        row = {'sample_id': '', 'grade': '2.5'}
        valid, errors = validate_csv_row(
            row,
            required_fields=['sample_id', 'grade']
        )
        # Returns: (False, ["Field 'sample_id' is missing or empty"])
    """
    # TODO: Implement this function
    # Check all required fields are present and non-empty
    # If numeric_fields provided, check each can be converted to float
    # Collect all errors and return (is_valid, errors)
    pass


def process_csv_with_validation(filepath: str) -> dict:
    """
    Process a CSV file, validating each row and reporting errors.

    Args:
        filepath: Path to the CSV file

    Returns:
        Dictionary with:
        - 'valid_rows': list of valid row dictionaries
        - 'invalid_rows': list of tuples (row_number, row, errors)
        - 'error_count': total number of invalid rows

    Example:
        result = process_csv_with_validation('data/samples.csv')
        print(f"Valid: {len(result['valid_rows'])}")
        print(f"Invalid: {result['error_count']}")
        for row_num, row, errors in result['invalid_rows']:
            print(f"Row {row_num}: {errors}")
    """
    # TODO: Implement this function
    # Define required fields: ['sample_id', 'rock_type', 'grade', 'depth']
    # Define numeric fields: ['grade', 'depth', 'mass']
    # Read CSV and validate each row using validate_csv_row
    # Track row numbers (1-based, excluding header)
    # Return summary dictionary
    pass


def safe_convert_numeric(value: str, default=None):
    """
    Safely convert a string to a float.

    Args:
        value: String to convert
        default: Value to return if conversion fails (default: None)

    Returns:
        Float value or default if conversion fails

    Example:
        grade = safe_convert_numeric('2.5')  # Returns 2.5
        grade = safe_convert_numeric('N/A', default=0.0)  # Returns 0.0
        grade = safe_convert_numeric('')  # Returns None
    """
    # TODO: Implement this function
    # Try to convert value to float
    # Return default if conversion fails
    pass


def check_file_exists(filepath: str) -> bool:
    """
    Check if a file exists and is readable.

    Args:
        filepath: Path to check

    Returns:
        True if file exists and is readable, False otherwise
    """
    # TODO: Implement this function
    # Try to open the file for reading
    # Return True if successful, False otherwise
    pass


def get_file_info(filepath: str) -> dict:
    """
    Get information about a file.

    Args:
        filepath: Path to the file

    Returns:
        Dictionary with file information or error details:
        - If file exists: {'exists': True, 'readable': True, 'line_count': N}
        - If file doesn't exist: {'exists': False, 'error': 'File not found'}
        - If permission denied: {'exists': True, 'readable': False, 'error': 'Permission denied'}
    """
    # TODO: Implement this function
    # Check if file exists and can be read
    # Count lines if readable
    # Return appropriate dictionary
    pass


# =============================================================================
# Test your code by running this file directly
# =============================================================================

if __name__ == "__main__":
    import os

    print("Testing error handling functions\n")

    # Test safe_read_file
    print("Testing safe_read_file:")
    # Uncomment to test:
    # success, result = safe_read_file('nonexistent.txt')
    # print(f"  Nonexistent file: success={success}, result={result}")

    # Test validate_csv_row
    print("\nTesting validate_csv_row:")
    test_rows = [
        {'sample_id': 'GEO-001', 'grade': '2.5', 'depth': '150'},
        {'sample_id': '', 'grade': '2.5', 'depth': '150'},
        {'sample_id': 'GEO-003', 'grade': 'invalid', 'depth': '150'},
    ]

    # Uncomment to test:
    # for row in test_rows:
    #     valid, errors = validate_csv_row(
    #         row,
    #         required_fields=['sample_id'],
    #         numeric_fields=['grade', 'depth']
    #     )
    #     print(f"  {row['sample_id'] or 'empty'}: valid={valid}, errors={errors}")

    # Test safe_convert_numeric
    print("\nTesting safe_convert_numeric:")
    # Uncomment to test:
    # print(f"  '2.5' -> {safe_convert_numeric('2.5')}")
    # print(f"  'N/A' -> {safe_convert_numeric('N/A', default=0.0)}")
    # print(f"  '' -> {safe_convert_numeric('')}")

    print("\nUncomment the test code above to test your implementation.")
