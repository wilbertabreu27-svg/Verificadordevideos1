from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Configuración: Dónde se guardarán temporalmente los videos para analizarlos
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ruta principal: Cuando alguien entra a tu página, le mostramos el diseño HTML
@app.route('/')
def home():
    # Flask buscará automáticamente el archivo index.html dentro de la carpeta "templates"
    return render_template('index.html')

# Ruta de análisis: El botón de tu diseño enviará los archivos a esta dirección oculta
@app.route('/analizar', methods=['POST'])
def analizar_media():
    # Verificamos si el navegador nos envió un archivo
    if 'file' not in request.files:
        return jsonify({"error": "No se envió ningún archivo"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "Nombre de archivo vacío"}), 400

    if file:
        # 1. Guardamos el archivo temporalmente
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # 2. AQUÍ IRÍA TU CÓDIGO DE ANÁLISIS REAL
        # Por ahora, vamos a simular que la inteligencia artificial lo revisó
        resultado_simulado = {
            "mensaje": f"El archivo {file.filename} ha sido analizado.",
            "es_original": True,
            "detalles": "No se detectaron cortes ni alteraciones en los metadatos."
        }
        
        # 3. Borramos el archivo para no llenar el servidor (opcional)
        os.remove(filepath)
        
        # 4. Le devolvems la respuesta a tu diseño web
        return jsonify(resultado_simulado)

if __name__ == '__main__':
    app.run(debug=True)
