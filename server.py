from flask import Flask, render_template
app = Flask(__name__, template_folder='home')

@app.route('/')
def home():
    return render_template("/index.html")



app.run(debug=True,port=5000)