from flask import Flask, g
from flask_cors import CORS
import mysql.connector
from login.login import login_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(login_bp)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)