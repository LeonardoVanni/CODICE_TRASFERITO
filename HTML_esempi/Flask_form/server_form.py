from flask import Flask, redirect, url_for, request

webapp = Flask(__name__)

@webapp.route('/successo/<nome>')
def benvenuto(nome):
    return 'Benvenuto {}!'.format(nome)

@webapp.route('/login', methods = ['POST', 'GET'])
def ingresso():
    if request.method == 'POST':
        utente = request.form['nome']
        return redirect(url_for('benvenuto', nome = utente))
    else:
        utente = request.args.get('nome')
        return redirect(url_for('benvenuto', nome = utente))

if __name__ == '__main__':
    webapp.run(debug=True)
