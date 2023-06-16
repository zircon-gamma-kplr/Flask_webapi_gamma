import flask
from flask import request, jsonify

# Création de l'objet Flask
app = flask.Flask(__name__)

# Lancement du Débogueur
app.config["DEBUG"] = True

# Quelques données tests pour l’annuaire sous la forme d’une liste de dictionnaires
employees = [{'id': 0,
              'Nom': 'Dupont',
              'Prénom': 'Jean',
              'Fonction': 'Développeur',
              'Ancienneté': '5'
              },
              {'id': 1,
               'Nom': 'Durand',
               'Prénom': 'Elodie',
               'Fonction': 'Directrice Commerciale',
               'Ancienneté': '4'
               },
               {'id': 2,
                'Nom': 'Lucas',
                'Prénom': 'Jérémie',
                'Fonction': 'DRH',
                'Ancienneté': '4'
                }
            ]

#décorateur
@app.route('/', methods=['GET'])
def home():
      return '''<h1>Annuaire Internet</h1><p>Ce site est le prototype d’une API mettant à disposition des données sur les employés d’une entreprise.</p>'''

# Route permettant de récupérer toutes les données de l’annuaire
@app.route('/api/v1/resources/employees/all', methods=['GET'])
def api_all():
      return jsonify(employees)

@app.route('/api/v1/resources/employees', methods=['GET'])
def api_id():
# Vérifie si un ID est fourni dans une URL
if 'id' in request.args:
      id = int(request.args['id'])
else:
      return "Erreur: Pas d’identifiant fourni. Veuillez spécifier un id."
        # Si un ID est fourni, il est affecté à une variable.
        # Si aucun ID n’est fourni, un message d’erreur est affiché dans le navigateur.
        # Crée une liste vide pour stocker les résultats
resultats = []
        
        # Boucle sur les données pour obtenir les résultats correspondant à l’ID fourni.
for employee in employees:
      if employee['id'] == id:
            resultats.append(employee)
        # Les IDs sont uniques, mais les autres champs peuvent renvoyer plusieurs résultats
        

# La fonction jsonify de Flask convertit notre liste de dictionnaires Python

# au format JSON return jsonify(results)


app.run()