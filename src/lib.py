import polars as pl


def read_dataset(file_path: str) -> pl.DataFrame:
    if file_path.endswith('.csv'):
        data = pl.read_csv(file_path, infer_schema_length=10000)
    elif file_path.endswith('.xlsx'):
        data = pl.read_excel(file_path, infer_schema_length=10000)
    else:
        raise ValueError("Unsupported file type")

    return data


def generate_summary_statistics(data: pl.DataFrame) -> dict:
    if data is None or data.shape[0] == 0:
        raise ValueError("Data cannot be None or empty")

    summary = {
        "mean": data.mean().to_dict(),
        "median": data.median().to_dict(),
        "std_dev": data.std().to_dict()
    }

    return summary
