import pandas as pd

def clean_data(input_file, output_file):
    # Load raw data
    df = pd.read_csv(input_file)
    
    # Example cleaning operations
    df.fillna(method='ffill', inplace=True)  # Fill missing values
    df.drop_duplicates(inplace=True)         # Remove duplicates
    
    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"Data cleaned and saved to {output_file}")

if __name__ == "__main__":
    # Specify file paths
    input_file = 'data/raw/Traffic_Crashes_-_Crashes.csv'
    output_file = 'data/processed/crashes_cleaned.csv'
    
    # Run the cleaning function
    clean_data(input_file, output_file)
