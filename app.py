from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('/register1.html')

app.route('/members_area')
def members_area():
    return render_template('members_area.html')



if __name__ =='__main__':
    app.run(debug=True)
