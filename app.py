from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')

def index():
    lectura = ""
    vector = []
    show = open("/home/lubuntu/Documentos/enfasis3/p7/flaskApp/info_monitor","r")
    for linea in show.readlines():
        lectura += linea
        vector.append(linea)
    show.close()
    return render_template("pagbase.html",l1=vector[0],l2=vector[1],l3=vector[2],l4=vector[3],l5=vector[4],l6=vector[5],l7=vector[6],l8=vector[7],l9=vector[8]) 

if __name__ == "__main__":
    app.run(debug=True)