# Server remoto per gestire un LED su raspberry PI
# il database statoRaspberry ci informa su quale sia lo stato di funzionamento attuale della PI

# GESTIONE DEL DATABASE statoRaspberry
# statoRaspberry è il db sqlite3 che contiene lo stato di PI

import sqlite3

# funzione per estrarre l'immagine da associare allo stato attuale del led
def estraiImmagine():
    db = sqlite3.connect('statoRaspberry')
    bufferDB = db.cursor()
    # nella tabella LED la colonna selettore indica quale è la riga dello stato attuale del led
    bufferDB.execute(''' SELECT FileImmagine FROM LED WHERE Selettore == 1  ''')
    estratto = bufferDB.fetchall()
    db.close()
    return estratto[0][0]

# funzione per aggiornare il selettore di stato del LED nel database
def aggiornaSelettore(ordine):
    if ordine == 'NIENTE':
        pass
    else:
        db = sqlite3.connect('statoRaspberry')
        bufferDB = db.cursor()
        bufferDB.execute(''' UPDATE LED SET Selettore = 0  ''')
        db.commit()
        if ordine == 'ACCENDI':
            bufferDB.execute(''' UPDATE LED SET Selettore = 1 WHERE StatoLED = 1  ''')
        if ordine == 'SPEGNI':
            bufferDB.execute(''' UPDATE LED SET Selettore = 1 WHERE StatoLED = 0 ''')
        db.commit()
        db.close()


# CREAZIONE DELLA WEBAPP
from flask import Flask, request, render_template, send_file

webapp = Flask(__name__)

ordineASAP = "NIENTE" # ordine da eseguire sulla pi

@webapp.route('/pannello', methods = ['GET','POST'])
def pannello():
    global ordineASAP
    if request.method == 'POST':
        ordineASAP = request.form['azioneLED']
        aggiornaSelettore(ordineASAP)
    return render_template('pannello.html', immagineLED = estraiImmagine())

@webapp.route('/immagini/<name>')
def servofile(name):
    name = 'immagini/' + name
    return send_file(name)

@webapp.route('/raspberry')
def raspy():
    global ordineASAP
    msg = ordineASAP
    ordineASAP = 'NIENTE'
    return msg

if __name__ == '__main__':
    webapp.run(host='0.0.0.0', debug=True)
