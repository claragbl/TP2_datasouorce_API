import uvicorn
import firebase_admin
from firebase_admin import credentials, firestore
from src.app import get_application

# Firebase Admin SDK
# cred = credentials.Certificate('api-projet-firebase-adminsdk.json')
# firebase_admin.initialize_app(cred)

app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app", debug=True, reload=True, port=8080)
