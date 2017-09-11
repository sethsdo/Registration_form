from flask import Flask, render_template, request, redirect,session, flash
import re
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

r = re.compile(r'[a-zA-Z]+')

dev = True

@app.route('/')
def my_portfolio():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create_info():
    for key in request.form.keys():
        print request.form[key]
        if len(request.form[key]) < 1:
            flash("All fields are required")
        elif not request.form['first_name'].isalpha(): 
            flash("Invalid  first name!")
        elif not request.form['last_name'].isalpha():
            print "ture"
            flash("Invalid Last Name!")
        elif len(request.form['password']) < 9:
            flash("Password must be more then 8 char!")
        elif request.form['confirm_password'] != request.form['password']: 
            flash("Passwords do not match!")
        else:
            session['email'] = request.form['email']
            session['first_name'] = request.form['first_name']
            session['last_name'] = request.form['last_name']
            session['password'] = request.form['password']
            session['confirm_password'] = request.form['confirm_password']
            return redirect('/about')
        return redirect('/')

@app.route('/about')
def show_user():
    print "Show user"
    return render_template('about.html', email=session['email'], first_name=session['first_name'], last_name=session['last_name'], password=session['password'])

@app.route('/back', methods=['GET'])
def back():
    return render_template('index.html')

app.run(debug=dev)
