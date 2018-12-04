from investment_resource import Homepage, Investments
from flask import Flask
from flask_restful import Api
from investment_model import Base
from db import engine

PORT = 8088
app = Flask(__name__)
api = Api(app)

if not engine.dialect.has_table(engine, "investments"):
    Base.metadata.create_all(engine)

api.add_resource(Homepage, '/')
api.add_resource(Investments, '/investments', '/investments/<int:id>')


if __name__ == "__main__":
    app.run(host='localhost', port=PORT, debug=True)
