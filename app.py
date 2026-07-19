from flask import Flask  # type: ignore
from routes.recomendacao import recomendacao_bp

app = Flask(__name__)

app.register_blueprint(recomendacao_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
