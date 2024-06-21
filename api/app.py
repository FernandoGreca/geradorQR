from flask import Flask, render_template, request
import pyqrcode
from pyqrcode import QRCode

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    try:
        link = (request.form['name'])
        return gerar(link)
    except ValueError:
        erro = "INFORME UM VALOR VALIDO!!"
        return render_template("index.html", erro=erro)
    
def gerar(link):
    
    qr_url = link

    qr_code = pyqrcode.create(qr_url)

    gerado = qr_code.png(file='qr_code.png', scale=8)
    
    return render_template("index.html", senha=gerado)


if __name__ == '__main__':
    app.run(debug=True)
