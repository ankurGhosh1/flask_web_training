from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.loan import LoanModel

class Loan(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('amount',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('agent_name',
                        type=str,
                        required=True,
                        help="Every loan needs a agent."
                        )

    @jwt_required()
    def get(self, name):
        loan = LoanModel.find_by_name(name)
        if loan:
            return loan.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if LoanModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Loan.parser.parse_args()

        loan = LoanModel(name, **data)

        try:
            loan.save_to_db()
        except:
            return {"message": "An error occurred inserting the loan."}, 500

        return loan.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, **data)

        item.save_to_db()

        return item.json()


class LoanList(Resource):
    def get(self):
        return {'loans': list(map(lambda x: x.json(), LoanModel.query.all()))}