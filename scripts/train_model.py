import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(input_file, model_output_file):
    # Load processed data
    df = pd.read_csv(input_file)
    
    # Define features and target
    X = df.drop('PRIMARY_CONTRIBUTORY_CAUSE', axis=1)
    y = df['PRIMARY_CONTRIBUTORY_CAUSE']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Save the trained model
    joblib.dump(model, model_output_file)
    print(f"Model trained and saved to {model_output_file}")

if __name__ == "__main__":
    # Specify file paths
    input_file = 'data/processed/merged_data.csv'
    model_output_file = 'models/random_forest_model.pkl'
    
    # Run the model training function
    train_model(input_file, model_output_file)
