from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Bienvenue sur l'application déployé via le HA Github, depuis l'image sur Dockerhub."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
