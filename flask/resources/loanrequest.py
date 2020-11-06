from flask_restful import Resource
from flask import request
from flask_jwt import jwt_required

from models.loan import LoanModel
#from models.loanemi import LoanEmi
 
class LoanEmi(Resource):
    @jwt_required
    def post(self):
        data = request.get_json()

        emi = LoanEmi(emi = data['emi'])
        emi.save_to_db()
        return data

        