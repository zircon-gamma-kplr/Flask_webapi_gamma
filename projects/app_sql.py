import flask
import psycopg2
import requests
from flask import request, url_for, jsonify
#connect to the PostgreSQL server
print('Connecting to the PostgreSQL database...')
conn = psycopg2.connect(dbname='wlcqcuzo',
                        user='wlcqcuzo',
                        password='s7aJFIA6upRM2rGNESNcZIDBAotLIpon',
                        host='horton.db.elephantsql.com'
                        )
# create a cursor
cur = conn.cursor()
#execute a statement
print('PostgreSQL database version:')
cur.execute('SELECT version()')
# display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)
# Instantiation de l'application
app = flask.Flask(__name__)
app.config["DEBUG"] = True
# Definition du format de sortie
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
        return d
# definition de l'ensemble des routes prises en charge par l'API
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Annuaire des employés</h1>
    <p>Prototype d'une API d'accès à la table employees de la base de données.</p>'''

@app.route('/api/v1/resources/employees/all', methods=['GET'])
def api_all():
    conn.row_factory = dict_factory
    all_employees = cur.execute('SELECT * FROM data;').fetchall
    return jsonify(all_employees)
def page_not_found(e):
    """ Fonction utilisée si la mauvaise route est spécifiée par un(e) utilisateur(-trice)"""
    return "<h1>404</h1><p>La ressource n'a pas été trouvée.</p>", 404

@app.route('/api/v1/resources/employees', methods=['GET'])
def api_filter():
    query_parameters = request.args
    id = query_parameters.get('id')
    name = query_parameters.get('name')
    value = query_parameters.get('value')
    query = "SELECT * FROM employees WHERE"
    to_filter = []
    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if value:
        query += ' value=? AND'
        to_filter.append(value)
            
app.run()


conn.commit()
	# close the communication with the PostgreSQL
        #cur.close()

    #finally:
        #if conn is not None:
            #conn.close()
            #print('Database connection closed.')
