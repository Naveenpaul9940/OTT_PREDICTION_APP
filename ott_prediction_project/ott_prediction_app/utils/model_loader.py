import os
import joblib
from huggingface_hub import hf_hub_download

MODEL_NAME = "dropoff_model.pkl"
REPO_ID = "naveen676767/ott-dropoff-model"

def load_model():
    model_path = hf_hub_download(
        repo_id=REPO_ID,
        filename=MODEL_NAME
    )
    return joblib.load(model_path)
