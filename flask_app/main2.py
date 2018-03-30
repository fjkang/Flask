from flask import Flask, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name, age, profession = "Jerry", 24, 'Programmer'
    template_context = dict(name=name, age=age , profession=profession)
    return render_template('index.html', **template_context)

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)

@app.route('/books/<genre>/')
def books(genre):
    res = make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    return res

if __name__ == "__main__":
    app.run(debug=True)