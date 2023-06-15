from flask import Flask, request
from datetime import datetime
import read_value_yf  

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello_world():
    if request.method == 'POST':
        # Aquí puedes manejar la lógica de tu solicitud POST
        # Puedes acceder a los datos enviados en la solicitud utilizando request.form, request.json, etc.
        # Por ejemplo, si se envía un JSON en la solicitud POST, puedes acceder a él así:
        data = request.json
        accion = data['accion']
        fecha_inicial = data['fecha_inicial']
        fecha_final = data['fecha_final']
        # Realiza las operaciones necesarias con los datos recibidos
        return read_value_yf.test(accion, fecha_inicial, fecha_final).to_json()
        
        # Retorna la respuesta al cliente

    # Si no es una solicitud POST, se manejará como antes
    return read_value_yf.test().to_json()

if __name__ == "__main__":
    print(f"{datetime.now()}")
    app.run(host="0.0.0.0")
