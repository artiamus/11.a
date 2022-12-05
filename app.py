from flask import Flask
import json
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
app.config["JSON_AS_ASCII"]=False
CORS(app)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/lasit')
def lasit():
    with open("chat.json", "r",encoding='utf-8') as f:
        zinas = f.read
    return zinas

@app.route('/sutit/<vards>/<zina>')
def sutit(vards,zina):
    tagad = datetime.now()
    laiks = tagad.strftime("%Y/%m/%d, %H:%M:%S")

    # print(vards,zina,laiks)

    rinda = {
        "zina":zina,
        "vards":vards,
        "laiks":laiks
    }

    with open("chat.json", "r",encoding='utf-8') as f:
        vecasZinas = f.read()
        vecieJson = json.loads(vecasZinas)

    vecieJson.append(rinda)


    with open ("chat.json", "w", encoding='utf-8') as f:
        json.dump(vecieJson,f,indent=2,ensure_ascii=False)

    return 'Ok'

@app.route('/datums')
def datums():
    return "Sodien ir 14.novembris"

@app.route('/lietotajs/<vards>/<vecums>')
def lietotajs(vards,vecums):
    #return f"{vards} un {vecums}"
    with open("lietotaji.json", "w",encoding="utf-8") as fails:
        return"OK"

app.run(host='0.0.0.0', port=81)