from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Bonjour je suis Chancy, une intelligence artificielle. Dites-moi comment je peux vous aider"
if __name__=="__main__"
    app.run(host="0.0.0.0", port=5000)
