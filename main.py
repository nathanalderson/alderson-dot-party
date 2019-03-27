from flask import *

app = Flask(__name__)

app.secret_key = r"\G)cTBS.iX3]&r6{:e'v5XNksS}5E:D6CP"

TAKEN = [4,11,15,21,22,37,38,50,51,55,84,89,92,94,110,122,144,150]

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/page-body", methods=['POST'])
def page_body():
    if request.form["password"] == "pickles":
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
