from flask import Flask , request
app = Flask(__name__)

stored_age = 26

@app.route('/')
def helloooo_world():
    return "Hello World!" 

@app.route('/sheela')
def sheela():
    global stored_age
    return "Sheela ki jawani!."

@app.route('/sheela/<age>')
def sheela_age(age):
    return f"Sheela ki umar {age}."

@app.route('/sheela', methods= ['POST'])
def sheela_post(age):
    global stored_age

    age= request.form.get('age')
    stored_age = age
    return "Done"




def sheela_age(age):
    return f"Sheela ki umar {age}."

app.run()