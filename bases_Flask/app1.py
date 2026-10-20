from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    titulo = "PWA"
    lista = ["Pedro","Julia","Regina"]
    return render_template("index.html", titulo = titulo, lista = lista)

@app.route("/operasBas", methods=["GET", "POST"])
def operasBas():
    n1 = 0
    n2 = 0
    res = 0
    operacion = ''
    
    if request.method == 'POST':
        n1 = request.form.get('n1')
        n2 = request.form.get('n2')
        
        if request.form.get("operacion") == 'sumar':
            res = float(n1) + float(n2)
        elif request.form.get("operacion") == 'restar':
            res = float(n1) - float(n2)
        elif request.form.get("operacion") == 'multiplicar':
            res = float(n1) * float(n2)
    return render_template("operasBas.html", n1=n1, n2=n2, res=res)

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    resultado = 0

    if request.method == 'POST':
        n1 = request.form.get('n1')
        n2 = request.form.get('n2')
        n3 = request.form.get('n3')
        n4 = request.form.get('n4')
        resultado = ((float(n3) - float(n1))**2 + (float(n4) - float(n2))**2) **0.5
    return render_template("distancia.html", n1=n1, n2=n2, n3=n3, n4=n4, resultado=resultado)

@app.route("/hola")
def func():
    return "Hola"

@app.route("/user/<string:user>")
def user(user):
    return "Hola desde /user " + user

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID: {} nombre: {}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma es: {}".format(n1 + n2)

if __name__ == "__main__":
    app.run(debug = True)