
# RA: 2200910 / Cleiton Jesus Barros Junior

from flask import Flask, jsonify, request
import mysql.connector

# Parametros de Conexão com o banco de dados
bancoDeDados = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sa123456",
  database="db_Alunos"
)

cursor = bancoDeDados.cursor()
tabela = 'tb_alunos'


app = Flask(__name__)

@app.route('/cadastrar', methods=['POST'])
def cadastrarAluno():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    matricula = request.form['matricula']
    insertSql = f"insert into {tabela} (nome, sobrenome, turma) values ('{nome}', '{sobrenome}', '{matricula}')"
    cursor.execute(insertSql)
    bancoDeDados.commit()
    return 'Aluno cadastrado com sucesso!'


@app.route('/listar', methods=['GET'])
def listarAlunos():
    selectAllSql = f"select * from {tabela}"
    cursor.execute(selectAllSql)
    resultado = cursor.fetchall()
    return jsonify(resultado)


@app.route('/deletar', methods=['DELETE'])
def deletarAluno():
    parametro = request.form['parametro']
    valor = request.form['valor']
    deleteSql = f"delete from {tabela} where {parametro} =  '{valor}'"
    cursor.execute(deleteSql)
    bancoDeDados.commit()
    return 'Aluno deletado com sucesso!'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
