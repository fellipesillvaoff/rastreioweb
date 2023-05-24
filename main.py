from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

@app.route("/resultado")
def resultado():
    nota_fiscal = request.args.get('nota')
    codigo_rastreamento = request.args.get('rastro')

    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_database = os.environ.get('DB_DATABASE')

    cnx = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_database
    )
    cursor = cnx.cursor()

    consulta = "SELECT * FROM rastreio WHERE nota_fiscal = %s AND rastreio = %s"
    valores = (nota_fiscal, codigo_rastreamento)
    cursor.execute(consulta, valores)

    resultado = cursor.fetchone()

    if cursor.rowcount > 0:
        # Extrair os dados do resultado da consulta
        nome_cliente = resultado[1]
        endereco = resultado[2]
        cep = resultado[3]
        separado = resultado[4]
        data_separado = resultado[5]
        coletado = resultado[6]
        data_coletado = resultado[7]
        entregue = resultado[8]
        previsto = resultado[9]
        rastreio = resultado[10]

        # Renderizar o template 'resultado.html' com os dados da consulta
        return render_template('resultado.html', nome_cliente=nome_cliente, endereco=endereco, cep=cep,
                               separado=separado, data_separado=data_separado, coletado=coletado,
                               data_coletado=data_coletado, entregue=entregue, previsto=previsto, rastreio=rastreio)
    else:
        return render_template('resultado.html', nome_cliente=None)

@app.route("/")
def homepage():
    return render_template('home.html')

@app.route("/consultar", methods=['GET'])
def consultar():
    nota_fiscal = request.args.get('nota')
    codigo_rastreamento = request.args.get('rastro')

    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_database = os.environ.get('DB_DATABASE')

    cnx = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_database
    )
    cursor = cnx.cursor()

    consulta = "SELECT * FROM rastreio WHERE nota_fiscal = %s AND rastreio = %s"
    valores = (nota_fiscal, codigo_rastreamento)
    cursor.execute(consulta, valores)

    resultado = cursor.fetchone()

    if cursor.rowcount > 0:
        # Extrair os dados do resultado da consulta
        nome_cliente = resultado[1]
        endereco = resultado[2]
        cep = resultado[3]
        separado = resultado[4]
        data_separado = resultado[5]
        coletado = resultado[6]
        data_coletado = resultado[7]
        entregue = resultado[8]
        previsto = resultado[9]
        rastreio = resultado[10]

        print("Dados do resultado:")
        print("Nome do cliente:", nome_cliente)
        print("Endereço:", endereco)
        print("CEP:", cep)
        print("Separado:", separado)
        print("Data de separação:", data_separado)
        print("Coletado:", coletado)
        print("Data de coleta:", data_coletado)
        print("Entregue:", entregue)
        print("Previsto:", previsto)
        print("Rastreio:", rastreio)

        # ... realizar verificações e atribuições necessárias ...

        return render_template('resultado.html', nome_cliente=nome_cliente, endereco=endereco, cep=cep,
                               separado=separado, data_separado=data_separado, coletado=coletado,
                               data_coletado=data_coletado, entregue=entregue, previsto=previsto, rastreio=rastreio)
    else:
        return render_template('resultado.html', nome_cliente=None)


if __name__ == "__main__":
    app.run()