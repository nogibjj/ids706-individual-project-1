from src.lib import read_dataset, generate_summary_statistics

if __name__ == "__main__":
    data = read_dataset('../notebooks/winequality-red.csv')
    summary = generate_summary_statistics(data)
    print(summary)
