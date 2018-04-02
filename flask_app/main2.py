from flask import Flask, make_response, render_template, request, redirect, url_for, flash
from flask_script import Manager
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
manager = Manager(app)

@app.route('/')
def index():
    name, age, profession = "Jerry", 24, 'Programmer'
    template_context = dict(name=name, age=age , profession=profession)
    return render_template('home.html', **template_context)

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)

@app.route('/books/<genre>/')
def books(genre):
    res = make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    return res

@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'root' and password == 'pass':
            message = "Correct username and password"
        else:
            message = "Wrong username or password"
    return render_template('login.html', message=message)

@app.route('/contact/', methods=['get', 'post'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(name)
        print(email)
        print(message)

        print("\nData received. Now redirecting ...")
        flash("Message Recived", "Success")
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)