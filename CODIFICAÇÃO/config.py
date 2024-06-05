import os
import app


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your_secret_key"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [os.path.join(os.path.dirname("app/templates/static"))]
