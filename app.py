
from flask import Flask, render_template
import sys

app = Flask(__name__)


@app.route('/')
def index():
	"""Renderiza la plantilla index.html ubicada en templates/"""
	return render_template('index.html')


if __name__ == '__main__':
	# Ejecuta la app en modo desarrollo por defecto. Si Flask no está instalado,
	# se lanzará un ImportError antes de llegar aquí.
	app.run(host='127.0.0.1', port=5000, debug=True)

