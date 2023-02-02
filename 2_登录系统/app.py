from flask import Flask, render_template,request 

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    name = request.args.get('name')
    return f'{name},欢迎登录！'

app.run(debug=True)