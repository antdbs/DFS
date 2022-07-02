from flask import Flask, render_template

## API flask
# input: (latitude, longitude)
# output: geojson du parcours

# 1. Récupere la liste des points d'opendata filtrer par l'utilisateur
    # contrainte temporelle,
    # contrainte moyen de transport,
    # contraite d'activité

# 2. Boucler sur tous ces points
    # 2.A Appeler l'api Valhalla
    # Garde le chemin plus cours

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('/form.html')


if __name__ == '__main__':
    app.run(debug=True)