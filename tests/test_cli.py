"""CLI tool test-suit."""

from git_helpers.cli import hello


def test_hello():
    assert hello("test") == "Hello test111"
