import pandas as pd

def create_features(input_file, output_file):
    # Load cleaned data
    df = pd.read_csv(input_file)
    
    # Example feature engineering
    df['NIGHT_DRIVING'] = df['CRASH_HOUR'].apply(lambda x: 1 if x >= 18 or x <= 6 else 0)
    df['IS_WEEKEND'] = df['CRASH_DAY_OF_WEEK'].apply(lambda x: 1 if x in [6, 7] else 0)
    
    # Save the data with new features
    df.to_csv(output_file, index=False)
    print(f"Feature engineered data saved to {output_file}")

if __name__ == "__main__":
    # Specify file paths
    input_file = 'data/processed/crashes_cleaned.csv'
    output_file = 'data/processed/merged_data.csv'
    
    # Run the feature engineering function
    create_features(input_file, output_file)
