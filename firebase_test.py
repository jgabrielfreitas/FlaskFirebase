from firebase import firebase
from respose import ResponseAPI
import json

# firebase = firebase.FirebaseApplication('https://usertestjgabrielfreitas.firebaseio.com/', None)
# new_user = '{ \"username\": \"jgabrielfreitas\", \"password\": \"jgaf1234\" }'
#
# result = firebase.post('/users', new_user)
# print result

response = ResponseAPI()
response.success = True
string_test = json.dumps(response.__dict__)
print(string_test)
