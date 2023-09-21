import pytest


def test_notebook():
    pytest.main(["--nbval", "../notebooks/polars.ipynb"])
