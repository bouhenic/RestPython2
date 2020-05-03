import json

from flask import Flask, request

from Request import Bdd

app = Flask(__name__)


@app.route('/<int:id>', methods=['GET'])
def requeteGetByid(id):
    bdd = Bdd('172.17.0.3', 3306, 'root', 'root', 'METEO')
    objet = json.loads(bdd.selectById(id))
    return objet


@app.route('/')
def requeteGetLastiD():
    bdd = Bdd('172.17.0.3', 3306, 'root', 'root', 'METEO')
    objet = json.loads(bdd.Lastselect())
    return objet

@app.route('/<int:id>', methods=['DELETE'])
def requeteDeleteByid(id):
    bdd = Bdd('172.17.0.3', 3306, 'root', 'root', 'METEO')
    bdd.delete(id)

    return "Enregistrement effacé"

@app.route('/', methods=['POST'])
def requetePost():
    TEMP = request.stream.read()
    bdd = Bdd('172.17.0.3', 3306, 'root', 'root', 'METEO')
    objet = json.loads(TEMP)
    temp = objet.get("temp")
    bdd.insert(temp)
    return "Enregistrement effectué"

@app.route('/<int:id>', methods=['PUT'])
def requeteUpdate(id):
    TEMP = request.stream.read()
    bdd = Bdd('172.17.0.3', 3306, 'root', 'root', 'METEO')
    objet = json.loads(TEMP)
    temp = objet.get("temp")
    bdd.update(temp,id)
    return "Enregistrement modifié"


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)
