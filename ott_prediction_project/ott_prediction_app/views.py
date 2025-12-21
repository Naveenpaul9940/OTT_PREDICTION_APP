from django.shortcuts import render
import joblib
import numpy as np
import os


model_path = os.path.join(os.path.dirname(__file__), "dropoff_model.pkl")
model = joblib.load(model_path)

def dropoff(request):
    prediction = None

    if request.method == "POST":
        watch_percentage = float(request.POST["watch_percentage"])
        episode_position = int(request.POST["episode_position"])
        cognitive_load = float(request.POST["cognitive_load"])
        pause_count = int(request.POST["pause_count"])
        rewind_count = int(request.POST["rewind_count"])

        input_data = np.array([watch_percentage,episode_position,cognitive_load,pause_count,rewind_count]).reshape(1, -1)

        prediction = model.predict(input_data)[0]

    return render(request, "prediction.html", {"prediction": prediction})

