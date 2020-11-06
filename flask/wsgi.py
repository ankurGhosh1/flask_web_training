from app import app
from db import db
    
db.init_app(app)

if __name__ == '__main__':
    ma.init_app(app)
    oauth.init_app(app)
    app.run()