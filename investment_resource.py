from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with
from flask import jsonify
from datetime import datetime
from investment_model import Investment
from db import session

get_parser = reqparse.RequestParser()
get_parser.add_argument('date', dest='creation_date', default=datetime.today().strftime('%Y-%m-%d'), help='Invested date')

parser = reqparse.RequestParser()
parser.add_argument('company', required=True, help='Invested Company')
parser.add_argument('quantity', type=int, required=True, help='Invested quantity')
parser.add_argument('cost', type=float, required=True, help='Invested cost')
parser.add_argument('creation_date', default=datetime.today().strftime('%Y-%m-%d'), help='Invested date')

investment_fields = {
    'id': fields.Integer,
    'company': fields.String,
    'quantity': fields.Integer,
    'cost': fields.Float,
    'creation_date': fields.String(default=datetime.today().strftime('%Y-%m-%d'))
}

class Homepage(Resource):
    def get(self):
        return jsonify({
            "Get the state of all investments on a given date": "GET /investments/<date>",
            "Create new investments": "POST /investments",
            "Update existing investments": "PUT /investments"
        })


class Investments(Resource):
    @marshal_with(investment_fields)
    def get(self):
        # if not date:
        #     date = datetime.today().strftime('%Y-%m-%d')
        parsed_args = get_parser.parse_args()
        date = parsed_args['creation_date']
        print(date)

        getByDateSQL = """SELECT company, sum(quantity) as total_quantity, sum(cost) as total_cost
FROM investments
WHERE creation_date < '{}'
GROUP BY company""".format(date)

        raw_investments = session.execute(getByDateSQL)

        investments = [{
            "company": row[0],
            "quantity":row[1],
            "cost":row[2]
        } for row in raw_investments]

        return investments

    @marshal_with(investment_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        investment = session.query(Investment).filter(Investment.id == id).first()
        investment.company = parsed_args['company']
        investment.quantity = parsed_args['quantity']
        investment.cost = parsed_args['cost']
        investment.creation_date = parsed_args['creation_date']
        session.add(investment)
        session.commit()
        return investment, 201

    @marshal_with(investment_fields)
    def post(self):
        parsed_args = parser.parse_args()
        investment = Investment(
            company=parsed_args['company'],
            quantity=parsed_args['quantity'],
            cost=parsed_args['cost'],
            creation_date=parsed_args['creation_date']
        )
        session.add(investment)
        session.commit()
        return investment, 201
