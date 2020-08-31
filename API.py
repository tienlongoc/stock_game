from flask import Flask, request, send_file
import fin_game

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    symbol = request.args.get("symbol")
    fin_game.process_symbol(symbol)
    return send_file("data/" + symbol + ".png", mimetype="image/png")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

