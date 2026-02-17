# lab4_text_io.py
"""
Lab 4 Task 1: Basic Text File I/O
Learn to read and write text files using context managers.

Learning Outcomes:
- LO4.1: Read and write text files using Python's built-in functions
- LO4.4: Use context managers (with statement) for file operations
"""


def write_sample_log(filepath: str, samples: list) -> int:
    """
    Write sample information to a log file.

    Args:
        filepath: Path to the output file
        samples: List of sample dictionaries with 'id', 'rock_type', 'grade'

    Returns:
        Number of lines written

    Example:
        samples = [
            {'id': 'GEO-001', 'rock_type': 'Granite', 'grade': 2.5},
            {'id': 'GEO-002', 'rock_type': 'Basalt', 'grade': 1.8}
        ]
        count = write_sample_log('output.txt', samples)
        # Creates file with:
        # Sample Log - Geological Survey
        # ========================================
        # Sample GEO-001: Granite, Grade: 2.5%
        # Sample GEO-002: Basalt, Grade: 1.8%
    """
    # TODO: Implement this function
    # Use 'with' statement to open file for writing ('w' mode)
    # Write header line: "Sample Log - Geological Survey"
    # Write separator line: "=" * 40
    # For each sample, write: "Sample {id}: {rock_type}, Grade: {grade}%"
    # Return total number of lines written (header + separator + samples)
    pass


def read_sample_log(filepath: str) -> list:
    """
    Read sample information from a log file.

    Args:
        filepath: Path to the input file

    Returns:
        List of lines from the file (excluding header and separator)

    Example:
        lines = read_sample_log('output.txt')
        # Returns ['Sample GEO-001: Granite, Grade: 2.5%', ...]
    """
    # TODO: Implement this function
    # Use 'with' statement to open file for reading ('r' mode)
    # Read all lines using readlines() or iterate through file
    # Skip header (first 2 lines)
    # Return list of sample lines (stripped of whitespace)
    pass


def append_to_log(filepath: str, message: str) -> None:
    """
    Append a message to an existing log file.

    Args:
        filepath: Path to the log file
        message: Message to append

    Returns:
        None

    Example:
        append_to_log('output.txt', 'Processing complete.')
    """
    # TODO: Implement this function
    # Use 'with' statement to open file in append mode ('a')
    # Write message followed by newline ('\n')
    pass


def count_lines(filepath: str) -> int:
    """
    Count the number of lines in a file.

    Args:
        filepath: Path to the file

    Returns:
        Number of lines in the file

    Example:
        num_lines = count_lines('output.txt')
        # Returns 4 (for file with header, separator, and 2 sample lines)
    """
    # TODO: Implement this function
    # Use 'with' statement to open and read file
    # Count and return number of lines
    # Hint: len(f.readlines()) or sum(1 for line in f)
    pass


def read_file_content(filepath: str) -> str:
    """
    Read and return the entire content of a file as a string.

    Args:
        filepath: Path to the file

    Returns:
        The entire file content as a string

    Example:
        content = read_file_content('output.txt')
    """
    # TODO: Implement this function
    # Use 'with' statement to open file
    # Use read() to get entire content
    pass


def write_lines(filepath: str, lines: list) -> int:
    """
    Write a list of strings to a file, each on a new line.

    Args:
        filepath: Path to the output file
        lines: List of strings to write

    Returns:
        Number of lines written

    Example:
        write_lines('notes.txt', ['Line 1', 'Line 2', 'Line 3'])
    """
    # TODO: Implement this function
    # Use 'with' statement to open file for writing
    # Write each line with a newline character
    # Return count of lines written
    pass


# =============================================================================
# Test your code by running this file directly
# =============================================================================

if __name__ == "__main__":
    # Test write_sample_log
    test_samples = [
        {'id': 'GEO-001', 'rock_type': 'Granite', 'grade': 2.5},
        {'id': 'GEO-002', 'rock_type': 'Basalt', 'grade': 1.8},
        {'id': 'GEO-003', 'rock_type': 'Sandstone', 'grade': 3.2}
    ]

    # Uncomment to test your implementation:
    # count = write_sample_log('test_log.txt', test_samples)
    # print(f"Wrote {count} lines")

    # lines = read_sample_log('test_log.txt')
    # print(f"Read {len(lines)} sample lines")

    # append_to_log('test_log.txt', '--- End of Log ---')

    # total = count_lines('test_log.txt')
    # print(f"Total lines: {total}")

    print("Uncomment the test code above to test your implementation.")
