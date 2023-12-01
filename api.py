import os
from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
from flask_restful import Resource, Api
from flask_bcrypt import Bcrypt

app = Flask(__name__, static_url_path='', static_folder='views/static', template_folder='views')   
mysql = MySQL(app)

# MySQL configurations
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_DB'] = 'PONTUAL'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

api = Api(app)

class FuncionarioResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            id_empresa = 1
            id_funcionario = 1
            id_evento = 0
            latitude = 0
            longitude = 0
            user_agent = data.get('user-agent')
            descricao = data.get('descricao')

            con = mysql.connect()
            cur = con.cursor()

            values = (id_empresa, id_funcionario, id_evento, latitude, longitude, user_agent, descricao)
            cur.execute(MyQueries.API_INSERT_APONTAMENTOS, values)

            con.commit()
            cur.close()
            con.close()

            return jsonify({"message": "Data updated successfully"})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

api.add_resource(FuncionarioResource, '/funcionario')
         
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 81))
    app.run(host='0.0.0.0', port=port, debug=True)

