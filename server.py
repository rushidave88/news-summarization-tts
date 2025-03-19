import uvicorn
from api import app  # Importing FastAPI app from api.py

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
