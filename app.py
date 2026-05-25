from flask import Flask, jsonify, request

app = Flask(__name__)
ALUMNOS_DB = [
    {"id": "20240001", "nombres": "Arturo Alejandro", "curso": "Programación Aplicada II", "ciclo": "V"},
    {"id": "20240002", "nombres": "Denzel Omar", "curso": "Programación Aplicada II", "ciclo": "V"}
]
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        "status": "online",
        "message": "Servidor Flask ejecutándose correctamente en Vercel",
        "version": "1.0.0",
        "entorno": "Producción Cloud"
    }), 200

@app.route('/api/alumnos', methods=['GET'])
def obtener_alumnos():
    codigo = request.args.get('codigo')
    if codigo:
        alumno = next((a for a in ALUMNOS_DB if a["id"] == codigo), None)
        if alumno:
            return jsonify({"success": True, "data": alumno}), 200
        return jsonify({"success": False, "error": "Alumno no encontrado"}), 404
        
    return jsonify({
        "success": True,
        "total": len(ALUMNOS_DB),
        "data": ALUMNOS_DB
    }), 200
if __name__ == '__main__':
    app.run(debug=True, port=5000)
