from log_report.utils.parser import parse_logs


def test_parse_valid_logs_from_multiple_files(make_log_file):
    """
    Test that logs are correctly parsed from multiple files.
    """
    file1 = make_log_file(
        ['{"url": "/a", "response_time": 0.1, "@timestamp": "2025-06-22T12:00:00"}']
    )
    file2 = make_log_file(
        ['{"url": "/b", "response_time": 0.2, "@timestamp": "2025-06-22T13:00:00"}']
    )

    logs = parse_logs([file1, file2])
    assert len(logs) == 2
    assert logs[0]["url"] == "/a"
    assert logs[1]["url"] == "/b"


def test_filter_by_date(make_log_file):
    """
    Test that logs are filtered by the provided date string.
    """
    file = make_log_file(
        [
            '{"url": "/a", "response_time": 0.1, "@timestamp": "2025-06-22T10:00:00"}',
            '{"url": "/b", "response_time": 0.2, "@timestamp": "2025-06-21T10:00:00"}',
        ]
    )

    logs = parse_logs([file], date_filter="2025-06-22")
    assert len(logs) == 1
    assert logs[0]["url"] == "/a"


def test_invalid_json_and_missing_fields(make_log_file):
    """
    Test that invalid JSON lines and logs missing required fields are ignored.
    """
    file = make_log_file(
        [
            "not-a-json",
            '{"no_url": true, "response_time": 0.1}',
            '{"url": "/ok", "response_time": 0.2}',
        ]
    )

    logs = parse_logs([file])
    assert len(logs) == 1
    assert logs[0]["url"] == "/ok"
