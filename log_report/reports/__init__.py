from log_report.reports.average import average

# Mapping of available report types to their corresponding handler functions.
REPORTS = {"average": average}


def get_report(name: str):
    """
    Retrieve a report handler function by report name.

    Args:
        name (str): The name of the report (e.g., "average").

    Returns:
        Callable: The report function corresponding to the given name.

    Raises:
        ValueError: If the report name is not registered.
    """
    if name not in REPORTS:
        raise ValueError(f"Unknown report type: {name}")
    return REPORTS[name]
