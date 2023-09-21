.PHONY: install format lint test

install:
    pip install -r requirements.txt

format:
    black src/ tests/

lint:
    ruff src/ tests/

test:
    pytest --nbval notebooks/polars.ipynb
    pytest tests/
