from collections import defaultdict


def average(logs):
    """
    Generate a report with the number of requests
    and average response time for each endpoint.

    Args:
        logs (list[dict]): List of parsed log entries,
        each containing 'url' and 'response_time'.

    Returns:
        list[dict]: List of dictionaries with 'endpoint',
        'count', and 'avg_time' fields.
    """
    stats = defaultdict(lambda: {"count": 0, "total_time": 0.0})

    for log in logs:
        endpoint = log["url"]
        time = log["response_time"]
        stats[endpoint]["count"] += 1
        stats[endpoint]["total_time"] += time

    return [
        {
            "endpoint": ep,
            "count": data["count"],
            "avg_time": round(data["total_time"] / data["count"], 4),
        }
        for ep, data in sorted(stats.items())
    ]
