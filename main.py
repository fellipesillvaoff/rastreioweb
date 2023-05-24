from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

@app.route("/resultado")
def resultado():
    nota_fiscal = request.args.get('nota')
    codigo_rastreamento = request.args.get('rastro')

    db_host = os.environ.get('DB_HOST',)
    db_port = int(os.environ.get('DB_PORT', '5810'))
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_database = os.environ.get('DB_DATABASE')

    cnx = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_database,
    )
    cursor = cnx.cursor()

    consulta = "SELECT * FROM rastreio WHERE nota_fiscal = %s AND rastreio = %s"
    valores = (nota_fiscal, codigo_rastreamento)
    cursor.execute(consulta, valores)

    resultado = cursor.fetchone()

    if resultado:
        nome_cliente = resultado[0]
        endereco = resultado[9]
        cep = resultado[10]
        Rseparado = resultado[3]
        data_separado = resultado[4]
        Rcoletado = resultado[5]
        data_coletado = resultado[6]
        Rentregue = resultado[7]
        previsto = resultado[8]
        cep=resultado[10]
        data_entrega=resultado[11]
        rastreio=resultado[2]

        if Rseparado == 1:
            separado = 'Separado'
        else:
            separado = ''

        if Rcoletado == 1:
            coletado='Separado'
        else:
            coletado=''
        if Rentregue == 1:
            entregue ="Entregue"
        else:
            entregue=''


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

        return render_template('resultado.html', nome_cliente=nome_cliente, endereco=endereco, cep=cep,
                               separado=separado, data_separado=data_separado, coletado=coletado,
                               data_coletado=data_coletado, entregue=entregue, previsto=previsto, rastreio=rastreio, data_entrega=data_entrega)
    else:
        return render_template('resultado.html', nome_cliente=None)

@app.route("/")
def homepage():
    return render_template('Home.html')

@app.route("/consultar", methods=['GET'])
def consultar():
    nota_fiscal = request.args.get('nota')
    codigo_rastreamento = request.args.get('rastro')

    db_host = os.environ.get('DB_HOST')
    db_port = int(os.environ.get('DB_PORT', '5810').strip("'"))
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_database = os.environ.get('DB_DATABASE')

    cnx = mysql.connector.connect(
        host='containers-us-west-127.railway.app',
        port='5810',
        user='root',
        password='SVMoPcKC8ybeb16LhjXz',
        database='railway'
    )
    cursor = cnx.cursor()

    consulta = "SELECT * FROM rastreio WHERE nota_fiscal = %s AND rastreio = %s"
    valores = (nota_fiscal, codigo_rastreamento)
    cursor.execute(consulta, valores)

    resultado = cursor.fetchone()

    if resultado:
        return render_template('resultado.html', nota_fiscal=nota_fiscal, codigo_rastreamento=codigo_rastreamento)
    else:
        return render_template('resultado.html', nota_fiscal=None, codigo_rastreamento=None)

app.debug = True
if __name__ == "__main__":
    app.run()
