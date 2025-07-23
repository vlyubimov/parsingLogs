import json


def is_valid_log(log):
    """
    Check whether a log entry contains required fields.

    Args:
        log (dict): A parsed log entry.

    Returns:
        bool: True if the log has 'url' and 'response_time' fields.
    """
    return isinstance(log, dict) and "url" in log and "response_time" in log


def matches_date(log, date_filter):
    """
    Check whether the log matches the given date (YYYY-MM-DD).

    Args:
        log (dict): A parsed log entry.
        date_filter (str or None): Date filter in format 'YYYY-MM-DD'.

    Returns:
        bool: True if the log matches the date or no date is provided.
    """
    if not date_filter:
        return True
    timestamp = log.get("@timestamp", "")
    return timestamp.startswith(date_filter)


def iter_log_lines(file_paths):
    """
    Yield stripped lines from multiple log files.

    Args:
        file_paths (list[str]): Paths to log files.

    Yields:
        str: A single line from one of the log files.
    """
    for path in file_paths:
        with open(path, encoding="utf-8") as f:
            for line in f:
                yield line.strip()


def parse_logs(file_paths, date_filter=None):
    """
    Parse log lines from files and return only
    valid entries (optionally filtered by date).

    Args:
        file_paths (list[str]): List of paths to log files.
        date_filter (str or None): Optional date to filter logs (format: 'YYYY-MM-DD').

    Returns:
        list[dict]: List of parsed and filtered log entries.
    """
    result = []

    for line in iter_log_lines(file_paths):
        try:
            log = json.loads(line)
        except json.JSONDecodeError:
            continue

        if not is_valid_log(log):
            continue
        if not matches_date(log, date_filter):
            continue

        result.append(log)

    return result
