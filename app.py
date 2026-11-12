from flask import Flask, render_template, request, session, redirect
from database import consultar_tarefas

app = Flask(__name__)
app.secret_key = "beca"

# Dados de acesso do ADMIN
ADMIN_EMAIL = "becamaciel.2111@gmail.com"
ADMIN_SENHA = "301295"

@app.route("/") # HomePage- Página Inicial
def home():
    if "login" not in session:
        return redirect("/login")
    
    #Usuário logado
    tarefas = consultar_tarefas()
    return render_template("index.html", tarefas=tarefas)

# ------------------------------------------------------------
# Rota de Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if "login" in session:
        return redirect("/")
    
    if request.method == "GET":
        return render_template("login.html")
    
    # POST
    email = request.form.get("email") # Pegando o email que estava no form HTLM 
    senha = request.form.get("senha") # Essaa informação estava no atributo name

    if email == ADMIN_EMAIL and senha == ADMIN_SENHA:
        session["login"] = True # Cria a sessão login
        return redirect("/") # Redireciona para a rota inicial
    else:
        return render_template ("login.html", msgerro ="E-mail ou senha estão incoretos!")

# ----------------------------------------------------------------
# Rota Logout
@app.route("/logout")
def logout():
    session.clear() # Apaga a lista sessão
    return redirect("/login")

# ----------------------------------------------------------------
# Tratamento de erro - Código 404
@app.errorhandler(404)
def not_found(erro):
    return render_template("erro404.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
    # host='0.0.0.0' Habilita o IP Público