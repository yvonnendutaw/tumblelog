from flask import Flask
#installs the mongodb extension
from flask.ext.mongoengine import MongoEngine

app=Flask(__name__)

#adds configuration of the database
app.config["MONGODB_SETTINGS"] = {'DB':"mydb"}
app.config["SECRET_KEY"] = "mysecret"

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from tumblelog.views import posts
    app.register_blueprint(posts)

register_blueprints(app)

if __name__ == '__main__':
	app.run(DEBUG=True)

