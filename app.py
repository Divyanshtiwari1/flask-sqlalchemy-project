from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Your app configuration goes here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'  # Replace with your actual database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your models, routes, etc.

@app.route('/')
def home():
    return "Hello, Flask is running!"

if __name__ == "__main__":
    # Update this to bind to all IP addresses and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)


