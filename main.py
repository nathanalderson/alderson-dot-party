from flask import *

app = Flask(__name__)

app.secret_key = r"\G)cTBS.iX3]&r6{:e'v5XNksS}5E:D6CP"

def get_taken():
    with open("taken.txt", 'r') as f:
        return [int(i) for i in f.read().split()]

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/page-body", methods=['POST'])
def page_body():
    if request.form["password"].lower() == "keller":
        return render_template('index2.html', taken=get_taken())
    else:
        abort(401)

@app.route("/bypass-password")
def bypass_password():
    if app.config['DEBUG']:
        return render_template('index.html',
                bypass_password=True,
                protected_content=render_template('index2.html', taken=get_taken()))
    else:
        abort(404)

@app.route("/demo")
def demo():
    return render_template('index-demo.html')
