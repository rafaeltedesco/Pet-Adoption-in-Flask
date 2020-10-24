from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li><a href='/animals/dogs'>Dogs</a></li>
    <li><a href='/animals/cats'>Cats</a></li>
    <li><a href='/animals/rabbits'>Rabbits</a></li>
  </ul>
  '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f'<h1>List of {pet_type}</h1>'
  html += '<ul>'
  for idx,pet in enumerate(pets.get(pet_type)):
    html += f"<li><a href='/animals/{pet_type}/{idx}'>{pet['name']}</a></li>"
  html += '</ul>'
  return html


@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets.get(pet_type)[pet_id]
  html = f"<h1>{pet['name']}</h1>"
  html += f"<img src={pet['url']} />"
  html += f"<p>{pet['description']}</p>"
  html += f"""
  <ul>
    <li>{pet['breed']}</li>
    <li>{pet['age']}</li>
  </ul>
  """
  return html

app.run(port='3003', host='0.0.0.0')