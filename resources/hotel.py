from flask_restful import Resource

lista_hoteis = [
    {"hotel_id": "sky", "nome": "Hotel Sky", "estrelas": 4.8, "diaria": 195.99, "cidade": "Porto"},
    {"hotel_id": "paraiso", "nome": "Hotel paraiso", "estrelas": 4.9, "diaria": 299.99, "cidade": "Lisboa"},
    {"hotel_id": "water", "nome": "Hotel water", "estrelas": 4.5, "diaria": 175.99, "cidade": "Famalicao"},
]

class Hoteis(Resource):
    def get(self):
        return { "hoteis": lista_hoteis }