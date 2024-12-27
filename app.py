from flask import Flask
import os

app = Flask(_name_)

@app.route("/")
def home():
    return "Hello, Flask!"

if _name_ == "_main_":
    port = 5000  
    if "PORT" in os.environ:
        port = int(os.environ["PORT"])
    
   
    app.run(debug=False, host="0.0.0.0", port=port)

