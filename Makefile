.PHONY: install format lint test

install:
    pip install -r requirements.txt

format:
    black src/ tests/

lint:
    ruff src/ tests/

test_notebook:
    pytest --nbval notebooks/polars.ipynb

test_script_lib:
    pytest tests/
