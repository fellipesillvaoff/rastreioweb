from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/resultado")
def resultado():
    nota_fiscal = request.args.get('nota')
    codigo_rastreamento = request.args.get('rastro')

    cnx = mysql.connector.connect(
        host="containers-us-west-127.railway.app",
        port='5810',
        user="root",
        password="SVMoPcKC8ybeb16LhjXz",
        database="railway"
    )
    cursor = cnx.cursor()

    consulta = "SELECT * FROM rastreio WHERE nota_fiscal = %s AND rastreio = %s"
    valores = (nota_fiscal, codigo_rastreamento)
    cursor.execute(consulta, valores)

    resultado = cursor.fetchone()

    if cursor.rowcount > 0:
        # Extrair os dados do resultado da consulta
        nome_cliente = resultado[0]
        endereco = resultado[9]
        cep = resultado[9]
        separado = resultado[3]
        data_separado = resultado[4]
        coletado = resultado[5]
        data_coletado = resultado[6]
        entregue = resultado[7]
        previsto = resultado[8]
        rastreio = resultado[9]

        # Renderizar o template 'resultado.html' com os dados da consulta
        return render_template('resultado.html', nome_cliente=nome_cliente, endereco=endereco, cep=cep,
                               separado=separado, data_separado=data_separado, coletado=coletado,
                               data_coletado=data_coletado, entregue=entregue, previsto=previsto, rastreio=rastreio)
    else:
        pass

@app.route("/")
def homepage():
    return render_template('home.html')

@app.route("/consultar", methods=['GET'])
def consultar():
    nota_fiscal = request.args.get('nota')
    codigo_rastreamento = request.args.get('rastro')

    cnx = mysql.connector.connect(
        host="containers-us-west-127.railway.app",
        port='5810',
        user="root",
        password="SVMoPcKC8ybeb16LhjXz",
        database="railway"
    )
    cursor = cnx.cursor()

    consulta = "SELECT * FROM rastreio WHERE nota_fiscal = %s AND rastreio = %s"
    valores = (nota_fiscal, codigo_rastreamento)
    cursor.execute(consulta, valores)

    resultado = cursor.fetchone()

    if cursor.rowcount > 0:
        # Extrair os dados do resultado da consulta
        nome_cliente = resultado[0]
        endereco = resultado[10]
        cep = resultado[10]
        separado = resultado[4]
        data_separado = resultado[5]
        coletado = resultado[6]
        data_coletado = resultado[7]
        entregue = resultado[8]
        previsto = resultado[9]
        rastreio = resultado[3]

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
        return render_template('resultado.html', nome_cliente=None)  # Ou tratar o caso em que nenhum resultado é encontrado


if __name__ == "__main__":
    app.run()
