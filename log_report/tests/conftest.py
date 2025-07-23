import tempfile

import pytest


@pytest.fixture
def make_log_file():
    """
    Create a temporary log file with the given list of log lines.

    Returns:
        Callable[[list[str]], str]: A function that takes a list of strings (log lines)
        and returns the path to the created temporary file.
    """

    def _make(lines: list[str]) -> str:
        f = tempfile.NamedTemporaryFile(mode="w+", delete=False, encoding="utf-8")
        for line in lines:
            f.write(line + "\n")
        f.flush()
        return f.name

    return _make
