import os
from kaggle.api.kaggle_api_extended import KaggleApi
import opendatasets as od

def get_kaggle_data():
    # od.download("https://www.kaggle.com/datasets/uciml/iris")

    # # Create the 'data/' folder if it doesn't exist
    # data_folder = '../data/'
    # if not os.path.exists(data_folder):
    #     os.makedirs(data_folder)

    # # Move the downloaded file to the 'data/' folder
    # shutil.move('Iris/Iris.csv', os.path.join(data_folder, 'Iris.csv'))

    # # Delete the 'Iris/' folder
    # shutil.rmtree('Iris/')

    # return 'ok'
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('uciml/iris', path='data/', unzip=True)

    return {"status": "Dataset downloaded successfully"}
