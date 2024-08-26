import pandas as pd

def load_data(file_path):
    """Load CSV data from a given file path."""
    return pd.read_csv(file_path)

def save_data(df, file_path):
    """Save DataFrame to a CSV file."""
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")
