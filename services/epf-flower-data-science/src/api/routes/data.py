# from services.data import get_kaggle_data
from src.services.data import get_kaggle_data
from fastapi import APIRouter

router = APIRouter()

@router.get("/data")
def get_data():
    try:
        get_kaggle_data()
    except:
        return "Error: couldn't download data."

    return 'ok'