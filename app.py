from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return '''
    <h1>💻 Avaliação Dev</h1>
    <form action="/resultado">
        <input type="text" name="nome" placeholder="Seu nome"><br><br>
        
        <label>Quanto tempo você programa?</label><br>
        <select name="tempo">
            <option value="iniciante">Menos de 3 meses</option>
            <option value="medio">3 a 12 meses</option>
            <option value="avancado">Mais de 1 ano</option>
        </select><br><br>

        <button type="submit">Ver resultado</button>
    </form>
    '''

@app.route("/resultado")
def resultado():
    nome = request.args.get("nome")
    tempo = request.args.get("tempo")

    if tempo == "iniciante":
        msg = "Tá começando, mas já tá no caminho certo 👊"
    elif tempo == "medio":
        msg = "Já tem base, bora subir de nível 🔥"
    else:
        msg = "Tá avançado, já pode buscar vaga 😏"

    return f"<h2>{nome}, {msg}</h2>"

if __name__ == "__main__":
    app.run()
