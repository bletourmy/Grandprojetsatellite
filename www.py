"""
 mini application web (utilisant le framework bottle)
 http://bottlepy.org/docs/dev/index.html
 
 debut d'interface pour le programme de calcul de coordonnees Satellites
 premiere version minimaliste tout en 1 fichier.

 pre-requis "bottle" installation via:
 pip install bottle

 lancer le serveur web integree via:
  python www.py

  puis ouvrir dans le browser via:
  http://localhost:8080


"""

from bottle import route, post, run, template, request

from obtenir_azimut_et_hauteur import spher_to_cart


@route('/')
def home():
    return '''
    <form action="/calcule" method="post">
    <h1> Visee d'un satellite </h1>
    <h3> (calcul de ses coordonnees horizontales pour l'observateur) </h3>
    <i>Position du satellite et de observateur en coordonnees spheriques</i>
    <h2> Satellite</h2>

            Altitude : <input name="r_s" type="text" />
            Longitude : <input name="theta_s" type="text" />
            Latitude : <input name="phi_s" type="text" />

    <h2> Observateur </h2>
            Altitude : <input name="r_s" type="text" />
            Longitude : <input name="theta_s" type="text" />
            Latitude : <input name="phi_s" type="text" />
    <br>  <br>
    <div>
            <input value="Calcule" type="submit" />
    </div>
        </form>
    '''

@post('/calcule')
def calcule():
    r_s = float(request.forms.get('r_s'))
    theta_s = float(request.forms.get('theta_s'))
    phi_s = float(request.forms.get('phi_s'))

    # exemple d'utilsation d'une fonction importee depuis obtenir_azimut_et_hauteur
    # le calcul n'est pas complet
    cart = spher_to_cart(r_s,theta_s,phi_s)

    return template('''
    <h1> Resultats </h1>
    Coordonnees speriques saisies: 
    <p> {{x}} {{y}} {{z}} </p>
    conversion en coordonnees carthesienns
    {{cart}}    
    ''', x=r_s, y=theta_s, z=phi_s, cart=cart)
                    

run(host='localhost', port=8080, debug=True)
