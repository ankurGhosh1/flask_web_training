from flask_restful import Resource
from flask_jwt import jwt_required
from flask import request
from marshmallow import ValidationError


from models.loan import LoanModel
from schema.loan import LoanSchema

loan_schema = LoanSchema()
allloan = LoanSchema(many=True)

class Loan(Resource):

    @jwt_required()
    def get(self, name):
        loan = LoanModel.find_by_name(name)
        if loan:
            return loan_schema.dump(loan)
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if LoanModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        loan_json = request.get_json()
        loan_json['name'] = name
        
        try: 
            loan = loan_schema.load(loan_json)
        except ValidationError as err:
            return err.messages, 400
        try:
            loan.save_to_db()
        except:
            return {"message": "An error occurred inserting the loan."}, 500

        return loan_schema.dump(loan), 201

    def delete(self, name):
        loan = LoanModel.find_by_name(name)
        if loan:
            loan.delete_from_db()
            return {'message': 'Loan deleted.'}
        return {'message': 'Loan not found.'}, 404

    def put(self, name):
        loan_json = request.get_json()
        loan = LoanModel.find_by_name(name)

        if loan:
            loan.amount = loan_json['amount']
            loan.agent_id = loan_json['agent_id']
        else:
            loan_json['name'] = name
            try: 
                loan = loan_schema.load(loan_json)
            except ValidationError as err:
                return err.messages, 400

        loan.save_to_db()

        return loan_schema.dump(loan)


class LoanList(Resource):
    def get(self):
        return {'loans': allloan.dump(LoanModel.find_all())}