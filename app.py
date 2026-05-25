from flask import Flask, jsonify

app = Flask(__name__)

ALUMNOS_DB = [
    {"id": "20240001", "nombres": "Arturo Alejandro", "curso": "Programación Aplicada II", "ciclo": "V"},
    {"id": "20240002", "nombres": "Denzel Omar", "curso": "Programación Aplicada II", "ciclo": "V"}
]

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "online",
        "message": "Servidor Flask ejecutándose correctamente en Vercel",
        "total_alumnos": len(ALUMNOS_DB),
        "data": ALUMNOS_DB
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)