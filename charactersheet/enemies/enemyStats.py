from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

app = (__name__)
app.config.from_pyfile('the-config-cfg')
db.init_app(app)

app.config['MONGODB_SETTING'] = {
    'db': 'videoGame',
    'host': 'localhost',
    'port': 42069
}

