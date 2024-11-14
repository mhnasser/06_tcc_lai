from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pag_inicial():
    
    return render_template("index.html")

@app.route("/mapa")
def pag_mapa():
    return render_template("mapa.html")

@app.route("/as_praticas")
def pag_praticas():
    return render_template("as_praticas.html")

@app.route("/quem_somos")
def pag_quem_somos():
    return render_template("quem_somos.html")

@app.route("/legislacao")
def pag_legislacao():
    return render_template("legislacao.html")

@app.route("/refs")
def pag_ref():
    return render_template("referencias.html")

# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)