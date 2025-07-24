import argparse
import sys

from log_report.reports import get_report
from tabulate import tabulate
from log_report.utils.parser import parse_logs


def main():
    """
    Parse command-line arguments, process log files, and display a report.

    Supported arguments:
    --file   List of log file paths (required)
    --report Report type to generate (required, e.g., 'average')
    --date   Optional date filter in 'YYYY-MM-DD' format

    The output is displayed in tabular format in the console.
    """
    parser = argparse.ArgumentParser(description="Log report generator")
    parser.add_argument("--file", nargs="+", required=True, help="Path to log file(s)")
    parser.add_argument(
        "--report", required=True, choices=["average"], help="Report type"
    )
    parser.add_argument("--date", help="Filter logs by date (YYYY-MM-DD)")

    args = parser.parse_args()

    try:
        logs = parse_logs(args.file, args.date)
        if not logs:
            print("There are no suitable logs to report.")
        report_func = get_report(args.report)
        report_data = report_func(logs)
        print(tabulate(report_data, headers="keys"))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
