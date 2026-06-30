from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Secure App!"

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Guest')
    # SOLUCIÓN DE SEGURIDAD: render_template_string sanitiza automáticamente
    # el parámetro 'name' mediante el motor Jinja2, neutralizando ataques XSS.
    template = '<h1>Hello, {{ name }}!</h1>'
    return render_template_string(template, name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)