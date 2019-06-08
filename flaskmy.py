from flask import Flask

app = Flask(__name__)

@app.route('/index/')
def landing_page():
    return 'This my flask web framework..Welcome..!!'


if __name__ == "__main__":
    app.run(debug = True)