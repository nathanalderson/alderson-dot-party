from flask import *

app = Flask(__name__)

app.secret_key = r"\G)cTBS.iX3]&r6{:e'v5XNksS}5E:D6CP"

TAKEN = [
    1, 2, 3, 4, 5, 6, 7, 8, 
    11, 12, 13, 15, 16, 19,
    20, 21, 22, 23, 24,
    30, 37, 38,
    41, 45, 48,
    50, 51, 55,
    68,
    75, 78,
    81, 84, 89,
    92, 94, 98,
    100, 110, 111,
    122,
    138,
    143,
    150,
]

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/page-body", methods=['POST'])
def page_body():
    if request.form["password"].lower() == "keller":
        return render_template('index2.html', taken=TAKEN)
    else:
        abort(401)

@app.route("/bypass-password")
def bypass_password():
    if app.config['DEBUG']:
        return render_template('index.html',
                bypass_password=True,
                protected_content=render_template('index2.html', taken=TAKEN))
    else:
        abort(404)

@app.route("/demo")
def demo():
    return render_template('index-demo.html')
