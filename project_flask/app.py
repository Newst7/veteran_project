from flask import Flask, render_template

app = Flask(__name__)

@app.route("/main")
def hello_world():
    return render_template('index.html')

@app.route("/reg")
def reg():
    return render_template('reg.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
