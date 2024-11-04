"""Autograding script."""

import os


def test_01():
    """Test word count job."""

    assert os.path.exists("files/output/summary.csv")
