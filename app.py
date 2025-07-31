from flask import Flask
from database.db import start_db 
from routes.routes import cliente_blueprint

app = Flask(__name__)

app.register_blueprint(cliente_blueprint)

if __name__ == '__main__':
    start_db()
    app.run(debug=True)