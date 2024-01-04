import pytest
from src.services.data import (
    get_kaggle_data, load_kaggle_data_json, process_species_data,
    split_dataset, train_and_save_model, make_prediction
)
import os
import joblib

class TestFunctions:
    def test_get_kaggle_data(self):
        """
        Test for the `get_kaggle_data` function.

        This test verifies that the `get_kaggle_data` function properly downloads the dataset from Kaggle and checks if the dataset file is created.

        Parameters:
            self (object): The instance of the test class.

        Returns:
            None
        """
        output = get_kaggle_data()
        assert output == {"status": "Dataset downloaded successfully"}
        assert os.path.exists('src/data/Iris.csv')

    def test_load_kaggle_data_json(self):
        """
        Test for the `load_kaggle_data_json` function.

        This test verifies that the `load_kaggle_data_json` function properly loads the dataset from the file and converts it to JSON.
        It checks if the returned value is a list and if a FileNotFoundError is correctly handled.

        Returns:
            None
        """
        try:
            output = load_kaggle_data_json()
            assert isinstance(output, list)
            
            os.rename('src/data/Iris.csv', 'src/data/Iris_temp.csv')
            output = load_kaggle_data_json()
            assert output == {"error": "Dataset file not found."}

        finally:
            # Rename the file back to its original name
            os.rename('src/data/Iris_temp.csv', 'src/data/Iris.csv')

    def test_process_species_data(self):
        """
        Test for the `process_species_data` function.

        This test case verifies that the `process_species_data` function properly processes the dataset and removes the 'Iris-' prefix from the 'Species' field.

        Returns:
            None
        """
        output = process_species_data()
        assert isinstance(output, list)
        
        for record in output:
            assert 'Species' in record
            assert not record['Species'].startswith('Iris-')

    def test_split_dataset(self):
        """
        Test for the `split_dataset` function.

        This test verifies that the `split_dataset` function properly splits the dataset into training and testing sets.
        It checks if the returned values are lists and if the sizes of the training and testing sets are correct (80% train 20% test).
        It also test if the features list for the training set et the label list for the training set have the same size (same for testing set).

        Returns:
            None
        """
        X_train, X_test, y_train, y_test = split_dataset()
        
        assert isinstance(X_train, list)
        assert isinstance(X_test, list)
        assert isinstance(y_train, list)
        assert isinstance(y_test, list)

        assert len(X_train) == len(y_train)
        assert len(X_test) == len(y_test)
        total_size = len(X_train) + len(X_test)

        assert abs(len(X_train) / total_size - 0.8) < 0.01
        assert abs(len(X_test) / total_size - 0.2) < 0.01

    def test_train_and_save_model(self):
        """
        Test for the `train_and_save_model` function.

        This test verifies that the `train_and_save_model` function properly saves the model to the correct location.
        It will check if the file 'src/models/KNN_model.pkl' is created after the function is run.
        It also check if the model has 'classes_' and 'n_estimators' attributes

        Returns:
            None
        """
        train_and_save_model()
        assert os.path.isfile('src/models/KNN_model.pkl')

        loaded_model = joblib.load('src/models/KNN_model.pkl')
        assert hasattr(loaded_model, 'classes_')
        assert hasattr(loaded_model, 'n_neighbors')

    def test_make_prediction(self):
        """
        Test for the `make_prediction` function.

        This test verifies that the `make_prediction` function returns a list and that the list contains the expected number of elements (1 specie).

        Returns:
            None
        """
        SepalLengthCm = 4.1
        SepalWidthCm = 3.8
        PetalLengthCm = 1.1
        PetalWidthCm = 0.3

        prediction = make_prediction(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)

        assert isinstance(prediction, list)
        assert len(prediction) == 1
