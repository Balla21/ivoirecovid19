from flask import Flask, render_template
from datetime import datetime
import requests
import json

app = Flask(__name__)

def getData(url):
    """fetch data from an url and return results """
    try:
        response = requests.get(url)
        return json.loads(response.text)
    except:
        return "404, Page Error"


@app.route("/")
def homepage() :
    civData = getData("https://corona.lmao.ninja/v2/countries/CIV?yesterday&strict&query")
    africaData = getData("https://corona.lmao.ninja/v2/continents/Africa?yesterday&strict")
    dateInfo = datetime.now()
    symptoms = ("fièvre", "toux sèche", "fatigue", "Essouflement", "courbatures et des douleurs", "congestion ‎nasale",
                 "maux de tête", "conjonctivite", "maux de gorge", "diarrhée", "perte ‎du goût ou de l’odorat",
                "éruption ‎cutanéeou une décoloration des doigts de la ‎main ou du pied")
    protections = ("se laver SYSTÉMATIQUEMENT les mains",
                   "prender au moins un mètre de distance avec les autres personnes")
    datas = {"civ": civData, "africa": africaData, "date": dateInfo, "symptoms": symptoms, "protections": protections}

    return render_template("index.html",data = datas)


if __name__ == "__main__" :
    app.run()
   
