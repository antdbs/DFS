from flask import Flask, render_template, request, jsonify
from dfs import get_parcours

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

@app.route("/getparcours", methods=['GET','POST'])
def get_path():
    if request.method == 'POST':
        data = request.json
        points = data["points"]
        dp = data["start_point"]
        costing = data["transport_type"]
        time = data["time"]
        result = get_parcours(points, dp, costing, time)
        points = [[48.87138948741586, 2.3008580899468396], [48.88614170811342, 2.341473214219776], [48.865533628765796, 2.3432659374724696]]
        result = get_parcours(points, [48.849442, 2.261198], "pedestrian", 1200)
    
    else:
        points = [[48.87138948741586, 2.3008580899468396], [48.88614170811342, 2.341473214219776], [48.865533628765796, 2.3432659374724696]]
        result = get_parcours(points, [48.849442, 2.261198], "pedestrian", 1200)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)