# questa è una webapp per accendere un led su raspberry pi

pict = ('pic_bulboff.gif', 'pic_bulbon.gif')

from flask import Flask, request, render_template, send_file

webapp = Flask(__name__)

@webapp.route('/', methods = ['GET','POST'])
def aggiorna():
    statoLED = 0 # inizializzazione del led, spento indicato come 0
    if request.method == 'POST':
        statoLED = eval(request.form['azioneLED'])
    print('lo stato del led è ', statoLED)
    return render_template('pannello.html', immagineLED = pict[statoLED])

@webapp.route('/<imma>')
def scegli_immagine(imma):
    return send_file(imma)

if __name__ == '__main__':
    webapp.run(host='0.0.0.0', debug=True)
