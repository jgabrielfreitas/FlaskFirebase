from flask import Flask
from flask import request
from user  import User
from firebase import firebase
from respose import ResponseAPI
import json


firebase = firebase.FirebaseApplication('https://usertestjgabrielfreitas.firebaseio.com/', None)
app = Flask(__name__)

@app.route("/insert-user", methods = ['POST'])
def insert_user():

    respose_api = ResponseAPI()
    result = firebase.post('/users', request.get_data())
    respose_api.success = True
    return json.dumps(respose_api.__dict__)

@app.route("/get-all-users", methods = ['GET'])
def get_info():
    return "{\"message\":\"get ok\"}"

def log(toLog):
    print("--> " + toLog)

if __name__ == "__main__":

    # user = User()
    # user.username = raw_input("Nome do usuario: ")
    # user.password = raw_input("Senha: ")
    #
    # print(user.as_json())

    log("Start running ....")
    app.run(debug=True)
    log("Stop application!")
