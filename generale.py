from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)


filename = 'data.txt'

from flask import Flask, render_template, request
import os


votanti = 0
filename = 'data.txt'
num_vot = [0]
lista_chiavi = ["Mazz5555", "18help10","irene2021","xxxx4444", "gdea1997","4V65YS1B","berlusconi6969", "penn2014","gcfm1502","daje1000", "step1992","mica3694","zoom4321", "pizz1317", "imec2019", "salv2003", "fato2120", "pdio2020", "Fdrcrll95", "Inference", "gcab1294","Inda1908","NYXC6789", "vacc6969", "Fluo8436","bari2017","ale123","dblm3680","albe1996", "Dand4567", "Figarasata01","dome1408", "sevi1518","cto123","PELI7001","prov1","prov4","prov3"]

lun_inizi = len(lista_chiavi)
riempi_voti = []

board = {}

@app.route('/')
def root():
    return render_template('pollprova.html')

    #return render_template('poll.html', data=poll_data)





@app.route('/pollprova', methods=['POST'])
def poll():
    #riempi_voti.clear()
    #board.clear()
    #vote = request.form['field']
    pres = request.form['pres']
    vice = request.form['vice']
    teso = request.form['teso']
    rapp = request.form['rapp']
    segre = request.form['segre']
    chiave  = request.form['field']





    if chiave in lista_chiavi:


             lista_chiavi.remove(chiave)
             votanti = lun_inizi - len(lista_chiavi)
             out = open(filename, 'a')


             out.write('votante ' + str(votanti) + '\n' + pres + '\n' + vice + '\n' + teso + '\n' + rapp + '\n' + segre + '\n\n')

             out.close()
             num_vot.append(votanti)
             print(votanti)

    #
             return render_template('thankyou.html')
    else:
             return "Chiave già utilizzata o non esistente"


   # return render_template('poll2.html', data=poll_data2)
    return render_template('thankyou.html')


@app.route('/results')
def show_results():

    nomi = ['Simone','Stefano','Riccardo','Irene','Jalena','Sonia']
    #votes = {}
    #for f in poll_data['fields']:
     #   votes[f] = 0

    #f = open(filename, 'r')
    with open(filename, 'r') as f:
        myNames = [line.strip() for line in f]

    print(myNames)
    #for line in f:
        #vote = line.rstrip("\n")
        #votes[vote] += 1
    diz = {}
    diz_no ={}

    #si_irene = myNames.count("Irene") + myNames.count("Si Irene, No Jalena")
    #si_jalena = myNames.count("Jalena") + myNames.count("Si Jalena, No Irene")



    diz["Simone"] = myNames.count("Simone")
    diz["Stefano"] = myNames.count("Stefano")
    diz["Riccardo"] = myNames.count("Riccardo")
    diz["Irene"] = myNames.count("Irene")
    diz["Jalena"] = myNames.count("Jalena")
    diz["Sonia"] = myNames.count("Sonia")

    diz_no["No Simone"] = myNames.count("No Simone")
    diz_no["No Stefano"] = myNames.count("No Stefano")
    diz_no["No Riccardo"] = myNames.count("No Riccardo")
    diz_no["No Irene"] = myNames.count("No entrambe")
    diz_no["No Jalena"] = myNames.count("No entrambe")
    diz_no["No Sonia"] = myNames.count("No Sonia")



    return render_template('results.html',  votes=diz, no= diz_no, vot = num_vot[-1])


if __name__ == "__main__":
    app.run(debug=True,  threaded = True)

