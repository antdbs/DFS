from flask import Flask, render_template, request
import json

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
def form():
    f = open('C:/Users/33660/PycharmProjects/DFS/activites.json', encoding='utf-8')
    data = json.load(f)

    return render_template('/form.html', markers=data)


def try_categories(request, name):
    try:
        return request.form[name]
    except:
        return "false"


@app.route("/forward/", methods=['POST'])
def get_data():
    data = {
        'request_content': [
            {
                'coordonees_x': '',
                'coordonees_y': '',
                'adresse': request.form['adresse'],
                'date_debut': request.form['start_time'],
                'date_fin': request.form['end_time'],
                'budget': request.form['budget'],
                'type_transport': request.form['transport'],
                'categories': {
                    'arts': try_categories(request, 'arts'),
                    'brocante': try_categories(request, 'brocante'),
                    'humour': try_categories(request, 'humour'),
                    'sciences': try_categories(request, 'sciences'),
                    'musique': try_categories(request, 'musique'),
                    'cinema': try_categories(request, 'cinema'),
                    'sport': try_categories(request, 'sport'),
                    'loisirs': try_categories(request, 'loisirs'),
                    'gourmand': try_categories(request, 'gourmand'),
                    'nature': try_categories(request, 'nature'),
                    'histoire': try_categories(request, 'histoire'),
                    'theatre': try_categories(request, 'theatre'),
                    'expo': try_categories(request, 'expo'),
                    'enfants': try_categories(request, 'enfants'),
                    'salon': try_categories(request, 'salon'),
                    'clubbing': try_categories(request, 'clubbing'),
                    'conference': try_categories(request, 'conference'),
                    'autre': try_categories(request, 'autre')
                }
            }
        ]
    }

    return data


if __name__ == '__main__':
    app.run()