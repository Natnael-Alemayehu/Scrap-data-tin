from flask import Flask
import script


app = Flask(__name__)
app.debug = False


@app.route("/")
def hello_world():

    return script.business_name_registered_number()
