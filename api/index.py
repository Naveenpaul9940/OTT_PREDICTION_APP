from vercel_wsgi import handle_wsgi
import ott_prediction_project.wsgi

app = ott_prediction_project.wsgi.application

handle_wsgi(app)
