from log_report.reports.average import average


def test_average_calculation():
    """
    Test that the 'average' report correctly calculates
    request count and average response time.
    """
    logs = [
        {"url": "/a", "response_time": 1.0},
        {"url": "/a", "response_time": 2.0},
        {"url": "/b", "response_time": 3.0},
    ]

    result = average(logs)
    expected = [
        {"endpoint": "/a", "count": 2, "avg_time": 1.5},
        {"endpoint": "/b", "count": 1, "avg_time": 3.0},
    ]

    assert all(item in result for item in expected)
