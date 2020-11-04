from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_migrate import Migrate
from flask_uploads import configure_uploads, patch_request_class
import os

from security import authenticate, identity
from resources.user import UserRegister
from resources.loan import Loan, LoanList
from resources.agent import Agent, AgentList
from resources.image import Image
from libs.image_helper import IMAGE_SET
from db import db
from ma import ma
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv(".env")
app.config.from_object("default_config")
# app.config.from_envvar("APPLICATION_SETTINGS")
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
#     "DATABASE_URI", "sqlite:///data.db"
# )
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'secret'
api = Api(app)
patch_request_class(app, 10 * 1024 * 1024)
configure_uploads(app, IMAGE_SET)
migrate = Migrate(app, db)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Agent, '/agent/<string:name>')
api.add_resource(AgentList, '/agents')
api.add_resource(Loan, '/loan/<string:name>')
api.add_resource(LoanList, '/loans')
api.add_resource(UserRegister, '/register')
api.add_resource(Image, '/upload')




if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000)