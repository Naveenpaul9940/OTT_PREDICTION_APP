from django.shortcuts import render
import numpy as np
import os
import joblib
from django.conf import settings


MODEL_PATH = os.path.join(settings.BASE_DIR,"ott_prediction_app","retention_risk_model.pkl")

model = joblib.load(MODEL_PATH)

def dropoff(request):
    prediction = None

    if request.method == "POST":
        episode_duration_min = float(request.POST["episode_duration_min"])
        pacing_score = float(request.POST["pacing_score"])
        hook_strength = float(request.POST["hook_strength"])
        avg_watch_percentage = float(request.POST["avg_watch_percentage"])
        pause_count = int(request.POST["pause_count"])
        rewind_count = int(request.POST["rewind_count"])
        skip_intro = int(request.POST["skip_intro"])
        cognitive_load = float(request.POST["cognitive_load"])
        drop_off_probability = float(request.POST["drop_off_probability"])

        input_data = np.array([
            episode_duration_min,
            pacing_score,
            hook_strength,
            avg_watch_percentage,
            pause_count,
            rewind_count,
            skip_intro,
            cognitive_load,
            drop_off_probability
        ]).reshape(1, -1)

        prediction = model.predict(input_data)[0]

        label_map = {0: "Low", 1: "Medium", 2: "High"}
        prediction = label_map.get(prediction, prediction)

    return render(request, "prediction.html", {"prediction": prediction})