from flask import Flask, render_template, url_for, request, session, redirect, g, jsonify

app = Flask(__name__)
app.secret_key='Hellothere'

@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)