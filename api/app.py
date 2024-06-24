from flask import Flask, render_template, request, send_file
import pyqrcode
import io

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
    
    qr_code = pyqrcode.create(link)
    
    buffer = io.BytesIO()
    qr_code.png(buffer, scale=10)
    buffer.seek(0)
    
    # Enviar o arquivo temporário
    return send_file(buffer, mimetype='image/png', download_name='qrcode.png')



if __name__ == '__main__':
    app.run(debug=True)
