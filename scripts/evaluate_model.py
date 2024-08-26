import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

def evaluate_model(model_file, test_data_file):
    # Load the trained model
    model = joblib.load(model_file)
    
    # Load test data
    df = pd.read_csv(test_data_file)
    X_test = df.drop('PRIMARY_CONTRIBUTORY_CAUSE', axis=1)
    y_test = df['PRIMARY_CONTRIBUTORY_CAUSE']
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Generate evaluation metrics
    print("Classification Report:\n", classification_report(y_test, y_pred))
    
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

if __name__ == "__main__":
    # Specify file paths
    model_file = 'models/random_forest_model.pkl'
    test_data_file = 'data/processed/merged_data.csv'
    
    # Run the model evaluation function
    evaluate_model(model_file, test_data_file)
