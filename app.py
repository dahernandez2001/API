from flask import Flask
from controllers.controllers import pelicula_bp

app = Flask(__name__)

# Registrar el blueprint de bandas
app.register_blueprint(pelicula_bp)

if __name__ == "__main__":
    app.run(debug=True)