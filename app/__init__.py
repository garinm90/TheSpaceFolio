from flask import Flask
import os
from os.path import basename
from config import Config




app = Flask(__name__)
app.config.from_object(Config)


from app import routes