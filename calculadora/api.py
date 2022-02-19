

from http.client import responses
import os
from flask import Flask, jsonify, request, render_template
from math import sqrt

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    return render_template('calculadora.html')

@app.route('/enviarform', methods=['POST'])
def calcular():
    v1 = request.form['valor_1']
    v2 = request.form['valor_2']
    operacao = request.form['valor_3']
    resultado = v1 + v2
    return str(resultado)



    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)