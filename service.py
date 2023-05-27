from flask import Flask, request
import requests

app = Flask(__name__)
service_url = 'http://localhost:5000'

@app.route('/cadastrar', methods = ['POST'])
def cadastrarAluno():
    response = requests.post(f'{service_url}/cadastrar', data=request.form)
    return response.text

@app.route('/listar', methods = ['GET'])
def listarAlunos():
    response = requests.get(f'{service_url}/listar', data=request.form)
    return response.json()

@app.route('/deletar', methods = ['DELETE'])
def deletarAluno():
    response = requests.delete (f'{service_url}/deletar', data=request.form)
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)