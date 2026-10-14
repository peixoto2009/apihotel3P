from flask import Flask
from flask_restful import Resource, Api
from resources.hotel import Hoteis

app = Flask(__name__)
api = Api(app)

#configuracao 

# rotas 
api.add_resource(Hoteis,"/hoteis")

#iniciar a aplicacao 
if __name__ == "__main__":
    app.run(debug=True)