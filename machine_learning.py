# machine_learning.py

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Function to train a machine learning model (simplified example)
def train_model(data):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data['features'], data['labels'], test_size=0.2)

    # Create and train a machine learning model (e.g., RandomForest)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    return model

# Function to evaluate network packet for threats using the trained model
def evaluate_model(model, packet):
    # Preprocess the packet (similar to preprocessing in data_preprocessing.py)
    preprocessed_packet = preprocess_data(packet)

    # Use the model to predict if it's a threat
    prediction = model.predict([preprocessed_packet])

    return prediction
