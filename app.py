from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, Mundo! Esta é minha aplicação na nuvem."

if __name__ == '__main__':
    app.run(debug=True)