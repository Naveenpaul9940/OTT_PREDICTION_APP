from gunicorn.app.wsgiapp import run
import ott_prediction_project.wsgi

if __name__ == "__main__":
    run()
