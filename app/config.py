import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

USER = 'app'
password_file = open('/run/secrets/password')
PASSWORD = password_file.readline().rstrip('\n')
DATABASE = 'app'

# Default Docker Compose network service name
HOSTNAME = 'db'

# Create the connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Build the Postgres ULI for SqlAlchemy

pg_url = 'postgresql://{0}:{1}@{2}/{3}' \
         .format(USER, PASSWORD, HOSTNAME, DATABASE)

# Configure the SqlAlchemy part of the app instance
app.config["SQLALCHEMY_ECHO"] = True
# app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config["SQLALCHEMY_DATABASE_URI"] = pg_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)
