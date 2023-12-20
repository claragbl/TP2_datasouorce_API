import os
from kaggle.api.kaggle_api_extended import KaggleApi
import opendatasets as od
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib
import json
import pickle
from sklearn.linear_model import LogisticRegression
from flask import Flask, request, jsonify
import logging

def get_kaggle_data():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('uciml/iris', path='src/data/', unzip=True)

    return {"status": "Dataset downloaded successfully"}

def load_kaggle_data_json():
    file_path = 'src/data/Iris.csv'
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient='records')
    except FileNotFoundError:
        return {"error": "Dataset file not found."}

def process_species_data():
    data = load_kaggle_data_json()
    for record in data:
        if 'Species' in record and record['Species'].startswith('Iris-'):
            record['Species'] = record['Species'].replace('Iris-', '')
    return data

def split_dataset():
    dataset = process_species_data()
    X_train, y_train, X_test, y_test = train_test_split(dataset, test_size=0.2, random_state=42)
    return X_train, y_train, X_test, y_test # len(train), len(test) 

def train_and_save_model():
    # split the dataset
    X_train, y_train, X_test, y_test = split_dataset()

    # load the parameter of the classifier (in model_parameters.json)
    with open('src/config/model_parameters.json') as f:
        parameters = json.load(f)

    n_neighbors = int(parameters[0]['n_neighbors']) 

    #train the KNeighbors model
    KNN_model = KNeighborsClassifier(n_neighbors=n_neighbors)
    KNN_model.fit(X_train, y_train)

    # Create models directory if it doesn't exist
    if not os.path.exists('src/models'):
        os.makedirs('services/epf-flower-data-science/src/models')

    # Save the model
    #pickle.dump(KNN_model, open('KNN_model.sav', 'wb'))
    joblib.dump(KNN_model, 'src/data/KNN_model.pkl')

    return KNN_model

def make_prediction(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
    model = train_and_save_model()
    predictions = model.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])
    logging(f"Predictions: {predictions}")
    return {"prediction": predictions[0]}



# def train_and_save_model():
#     try:
#         # Load dataset
#         dataset = pd.read_csv('src/data/Iris.csv')

#         # Load parameters from JSON
#         with open('services/epf-flower-data-science/src/config/model_parameters.json', 'r') as f:
#             model_params = json.load(f)

#         # Dropping 'Id' and using 'Species' as the target variable
#         X = dataset.drop(['Id', 'Species'], axis=1)  # Drop 'Id' column
#         y = dataset['Species']  # Target variable

#         # Split dataset using split_dataset function
#         X_train, X_test, y_train, y_test = split_dataset()

#         model = LogisticRegression(**model_params)  # Instantiate model with given params

#         model.fit(X_train, y_train)  # Train the model

#         # Save the trained model
#         joblib.dump(model, 'src/data/trained_model.pkl')

#         return {"status": "Model trained and saved successfully"}

#     except Exception as e:
#         return {"error": f"Error training model: {e}"}