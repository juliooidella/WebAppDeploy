from flask import Flask, render_template
from asgiref.wsgi import WsgiToAsgi
import pandas as pd


app = Flask(__name__)


@app.route("/inicio")
def home():
    df = pd.read_csv("tabela - livros.csv")
    lista = df["Titulo do Livro"].tolist()
    return render_template(
        "lista.html", titulo="Lista de Livros", lista_de_livros=lista
    )


@app.route("/curriculo")
def curriculo():
    return render_template("curriculo.html")


asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    app.run()
