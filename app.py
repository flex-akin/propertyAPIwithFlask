from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from sqlalchemy.ext.automap import automap_base
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ivantageAdmin:ivantagedb@3.227.55.23/propertydb'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

#init database
db = SQLAlchemy(app)

#init marshmallow
ma = Marshmallow(app)
with app.app_context():
    Base = automap_base()
    Base.prepare(db.engine)
    Area = Base.classes.Area


@app.route('/')
def index():
    results = db.session.query(Area).all()
    for i in results:
    
        return jsonify(i.area)

    





if __name__ == "__main__":
    app.run(port= 3030, debug=True)

