from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.dojos import Dojos 
from flask_app.models.ninjas import Ninjas


@app.route("/")
def home():
    return redirect ('/all_dojos')

@app.route ('/all_dojos')
def all_dojos():
    dojos = Dojos.get_all()
    return render_template ("dojos.html", dojos = dojos)

@app.route('/new_dojo', methods = ['POST'])
def add_dojo():
    new_dojo ={
    "name": request.form["name"]
    }
    print(request.form)
    Dojos.save_dojo(new_dojo)
    return redirect('/all_dojos')

@app.route("/add_ninja")
def new_ninja():
    dojos = Dojos.get_all()
    return render_template ("ninjas.html", dojos = dojos)

@app.route('/ninjas', methods = ['POST'])
def input():
    # user_data = {
    # "first_name": request.form["first_name"],
    # "last_name": request.form["last_name"],
    # "age": request.form["age"]
    #     } tried this first and wasnt working.
    Ninjas.save(request.form)
    return redirect("/")

@app.route('/single_dojo/<int:id>')
def view_dojos_with_ninjas(id):
    data={
        "id": id
    }
    logged_dojo = Dojos.dojo_with_ninjas(data)
    
    return render_template('show_ninjas.html', one_dojo = logged_dojo)