# lab4_data_processor.py
"""
Lab 4 Task 4: Processing Geological CSV Data
Apply file I/O skills to analyze geological sample data.

Learning Outcomes:
- LO4.1: Read and write text files using Python's built-in functions
- LO4.2: Process CSV files using the csv module
- LO4.4: Use context managers (with statement) for file operations
"""

import csv


def calculate_statistics(filepath: str, column: str) -> dict:
    """
    Calculate basic statistics for a numeric column.

    Args:
        filepath: Path to the CSV file
        column: Name of the numeric column

    Returns:
        Dictionary with 'count', 'sum', 'mean', 'min', 'max'
        Values should be rounded to 2 decimal places where applicable

    Example:
        stats = calculate_statistics('data/samples.csv', 'grade')
        # {'count': 50, 'sum': 125.5, 'mean': 2.51, 'min': 0.5, 'max': 4.8}
    """
    # TODO: Implement this function
    # Read the CSV file using DictReader
    # Extract numeric values from the specified column
    # Skip rows where the value cannot be converted to float
    # Calculate count, sum, mean, min, max
    # Return dictionary with statistics (round to 2 decimal places)
    pass


def group_by_location(filepath: str) -> dict:
    """
    Group samples by their location.

    Args:
        filepath: Path to the CSV file

    Returns:
        Dictionary with location as key and list of sample_ids as value

    Example:
        groups = group_by_location('data/samples.csv')
        # {'Site-A': ['GEO-001', 'GEO-005', ...], 'Site-B': ['GEO-002', ...]}
    """
    # TODO: Implement this function
    # Read CSV using DictReader
    # Create a dictionary to group sample_ids by location
    # Return the dictionary
    pass


def find_high_grade_samples(filepath: str, threshold: float) -> list:
    """
    Find samples with grade above the threshold.

    Args:
        filepath: Path to the CSV file
        threshold: Minimum grade value (exclusive)

    Returns:
        List of dictionaries for high-grade samples, sorted by grade (descending)

    Example:
        high_grade = find_high_grade_samples('data/samples.csv', 3.0)
        # [{'sample_id': 'GEO-023', 'grade': '4.5', ...}, ...]
    """
    # TODO: Implement this function
    # Read CSV using DictReader
    # Filter samples where float(grade) > threshold
    # Sort by grade in descending order
    # Return list of sample dictionaries
    pass


def count_by_rock_type(filepath: str) -> dict:
    """
    Count the number of samples for each rock type.

    Args:
        filepath: Path to the CSV file

    Returns:
        Dictionary with rock_type as key and count as value

    Example:
        counts = count_by_rock_type('data/samples.csv')
        # {'Granite': 12, 'Basalt': 8, 'Sandstone': 15, ...}
    """
    # TODO: Implement this function
    # Read CSV and count occurrences of each rock type
    pass


def calculate_average_by_group(filepath: str, group_column: str,
                                value_column: str) -> dict:
    """
    Calculate average of a numeric column grouped by another column.

    Args:
        filepath: Path to the CSV file
        group_column: Column to group by (e.g., 'location', 'rock_type')
        value_column: Numeric column to average (e.g., 'grade', 'depth')

    Returns:
        Dictionary with group values as keys and average as values

    Example:
        avg_by_location = calculate_average_by_group(
            'data/samples.csv', 'location', 'grade'
        )
        # {'Site-A': 2.45, 'Site-B': 3.12, 'Site-C': 1.89}
    """
    # TODO: Implement this function
    # Read CSV and group numeric values by the group column
    # Calculate average for each group
    # Return dictionary with averages (rounded to 2 decimal places)
    pass


def generate_summary_report(filepath: str, output_path: str) -> None:
    """
    Generate a text summary report of the sample data.

    Args:
        filepath: Path to the input CSV file
        output_path: Path to the output text file

    The report should include:
    - Total number of samples
    - Number of unique locations
    - Number of unique rock types
    - Grade statistics (min, max, mean)
    - Top 5 highest grade samples

    Example output:
    ================================
    GEOLOGICAL SAMPLE SUMMARY REPORT
    ================================

    Overview:
    - Total samples: 50
    - Unique locations: 3
    - Unique rock types: 5

    Grade Statistics:
    - Minimum: 0.45
    - Maximum: 4.82
    - Mean: 2.51

    Top 5 Highest Grade Samples:
    1. GEO-023: 4.82 (Granite, Site-A)
    2. GEO-041: 4.65 (Basalt, Site-B)
    ...
    """
    # TODO: Implement this function
    # Read and analyze the CSV data
    # Calculate various statistics
    # Write a formatted summary report to the output file
    pass


def find_depth_range_samples(filepath: str, min_depth: int, max_depth: int) -> list:
    """
    Find samples within a specified depth range.

    Args:
        filepath: Path to the CSV file
        min_depth: Minimum depth (inclusive)
        max_depth: Maximum depth (inclusive)

    Returns:
        List of sample dictionaries within the depth range

    Example:
        samples = find_depth_range_samples('data/samples.csv', 100, 200)
    """
    # TODO: Implement this function
    # Read CSV and filter by depth range
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
        # stats = calculate_statistics(data_path, 'grade')
        # print(f"Grade statistics: {stats}")

        # groups = group_by_location(data_path)
        # for loc, samples in groups.items():
        #     print(f"{loc}: {len(samples)} samples")

        # high_grade = find_high_grade_samples(data_path, 3.5)
        # print(f"\nHigh-grade samples (>3.5): {len(high_grade)}")
        # for s in high_grade[:3]:
        #     print(f"  {s['sample_id']}: {s['grade']}")

        # generate_summary_report(data_path, 'summary_report.txt')
        # print("\nSummary report generated!")

        print("Uncomment the test code above to test your implementation.")
    else:
        print(f"Data file not found: {data_path}")
        print("Run this file from the repository root directory.")
