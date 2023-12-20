# from services.data import get_kaggle_data
from src.services.data import get_kaggle_data, load_kaggle_data_json, process_species_data
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