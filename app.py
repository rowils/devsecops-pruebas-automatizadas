from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    # Captura el parámetro 'name' directamente desde la URL
    name = request.args.get('name', 'Guest')
    
    # VULNERABILIDAD CRÍTICA (XSS): Se concatena el input sin sanitizar en un string HTML
    return f"<h1>Hello, {name}!</h1>"

if __name__ == '__main__':
    # La aplicación corre en modo debug activo (No recomendado para producción)
    app.run(host='0.0.0.0', port=5000, debug=True)