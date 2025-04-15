from flask import Flask, request, jsonify

app = Flask(__name__)

# Parametry modelu regresji liniowej (przykładowe)
wagi = [2.5, -1.0]  # współczynniki regresji
intercept = 10.0    # wyraz wolny
prog_decyzyjny = 20.0  # próg decyzyjny

@app.route('/decyzja', methods=['GET'])
def decyzja():
    try:
        # Pobieramy dane wejściowe z zapytania
        x1 = float(request.args.get('x1'))
        x2 = float(request.args.get('x2'))

        # Obliczamy y_hat = w1*x1 + w2*x2 + b
        y_hat = wagi[0]*x1 + wagi[1]*x2 + intercept

        # Reguła decyzyjna
        decyzja = "Pozytywna decyzja" if y_hat > prog_decyzyjny else "Negatywna decyzja"

        return jsonify({
            "x1": x1,
            "x2": x2,
            "y_hat": y_hat,
            "decyzja": decyzja
        })
    except (TypeError, ValueError):
        return jsonify({"error": "Błąd w danych wejściowych. Użyj parametrów x1 i x2 jako liczby."}), 400

if __name__ == '__main__':
    app.run(debug=True)