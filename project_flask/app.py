from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/main")
def index():

    return render_template('index.html')
@app.route("/user/<username>")
def profile(username):

    return f'{username}\'s profile'
@app.route("/reg")
def reg():
    
    return render_template('registration.html')
@app.route("/sup")
def support():

    return render_template('support.html')
@app.route("/job")
def job():

    return render_template('job.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
