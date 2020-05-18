from flask import Flask

app = Flask(__name__)

from api.cpf.views import cpf

app.register_blueprint(cpf)