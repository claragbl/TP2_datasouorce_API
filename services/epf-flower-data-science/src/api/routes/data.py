# from services.data import get_kaggle_data
from src.services.data import get_kaggle_data, load_kaggle_data_json, process_species_data, split_dataset, train_and_save_model, make_prediction
from fastapi import APIRouter

router = APIRouter()

@router.get("/data")
def get_data():
    try:
        get_kaggle_data()
    except:
        return "Error: couldn't download data."

    return 'ok'

@router.get("/data/dowload")
def load_data():
    try:
        dataset =load_kaggle_data_json()
    except:
        return "Error: couldn't download data in JSON format."

    return dataset

@router.get("/data/process")
def process_data():
    try:
        dataset = process_species_data()
    except:
        return "Error: couldn't process the data."

    return dataset

@router.get("/data/split")
def split_data():
    try:
        train, test = split_dataset()
    except:
        return "Error: couldn't split the data."

    return train, test

@router.get("data/train")
def train_model():
    try:
        train_and_save_model()
    except:
        return "Error: couldn't train the model."

    return "ok"

@router.get("data/prediction")
def predict(SepalLengthCm: float, SepalWidthCm: float, PetalLengthCm: float, PetalWidthCm: float):
    try: 
        make_prediction(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    except:
        return "Error: couldn't make the prediction."