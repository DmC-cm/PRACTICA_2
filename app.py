from flask import Flask,render_template,request,url_for,redirect

app=Flask(__name__)

@app.route ("/")
def index():
    return render_template("index.html")
@app.route ("/info1")
def info1():
    return render_template("info1.html")

@app.route("/form1",methods=['POST','GET'])
def  fomr1():
    if request.method =='POST': #si es una llamada del formulario
        nombre=request.form.get('nombre')
        apellidos=request.form.get('apellidos')
        curso=request.form.get('select')
        return render_template("info1.html",nombre=nombre,apellidos=apellidos,curso=curso)
    return render_template("/")

@app.route("/form2",methods=['POST','GET'])
def  fomr2():
    if request.method =='POST': #si es una llamada del formulario
        nombre=request.form.get('nombreru')
        apellidos=request.form.get('apellidosru')
        correo=request.form.get('emailru')
        contraseña=request.form.get('contraseñaru')
        return render_template("info2.html",nombre=nombre,apellidos=apellidos,correo=correo,contraseña=contraseña)
    return render_template("/")

@app.route("/form3",methods=['POST','GET'])
def  fomr3():
    if request.method =='POST': #si es una llamada del formulario
        nombre=request.form.get('nombrepro')
        categoria=request.form.get('selectpro')
        existencias=request.form.get('existencias')
        precio=float(request.form.get('precio'))
        return render_template("info3.html",nombre=nombre,categoria=categoria,existencias=existencias,precio=precio)
    return render_template("/")

@app.route("/form4",methods=['post'])
def form4():
    if request.method=='POST':
        titulo=request.form.get("titulo")
        autor=request.form.get("autor")
        desc=request.form.get("desc")
        medio=request.form.get("opcion")
        return render_template("info4.html",titulo=titulo,autor=autor,desc=desc,medio=medio)
    return render_template("/")
if  __name__ =="__main__":
    app.run(debug=True)