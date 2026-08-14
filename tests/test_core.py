"""Tests for quantum-leaf."""
from quantum.core import run


def test_run():
    result = run()
    assert result.ok
