from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from sqlalchemy.ext.automap import automap_base
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

#init database
db = SQLAlchemy(app)

#init marshmallow
ma = Marshmallow(app)
with app.app_context():
    Base = automap_base()
    Base.prepare(db.engine)
    Area, Property = Base.classes.Area, Base.classes.Property


class AreaSchema(ma.Schema):
  class Meta:
    fields = ('areaId', 'area', 'stateId')

# Init schema
area_schema = AreaSchema()
areas_schema = AreaSchema(many=True)


class PropertySchema(ma.Schema):
  class Meta:
        fields = ( "id", "propertyCode", "developer", "projectName","completionDate", "mapLocation", "state", "area", "propertyType", "numberOfBedrooms", "numberOfWashrooms", "description", "availableUnits", "totalUnits", "price", "propertySize" , "propertyFeatures" ,"status", "businessType", "businessName", "flyer", "video", "images")

property_schema = PropertySchema()
properties_schema = PropertySchema(many=True)


@app.route('/property', methods=['GET'])
def index():

   # allProdcuts = db.session.execute(db.select(Area).filter_by(area='Lagos')).scalar_one()
   # allProdcuts = db.session.execute(db.select(Area).all()



    all_properties = db.session.query(Property).all()
    result = properties_schema.dump(all_properties)
    
    resp = { "data" : result , "message" : "success"}
    myResponse = make_response( jsonify(resp) )
    myResponse.headers['customHeader'] = 'This is a custom header'
    myResponse.status_code = 201
    return myResponse


if __name__ == "__main__":
    app.run(port= 3030, debug=True)

