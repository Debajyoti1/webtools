from flask import Flask, render_template, url_for, request, session, redirect, g, jsonify
from selenium import webdriver
import os
def r():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get('https://gadgetguys.in')
    print(driver.title)
app = Flask(__name__)
app.secret_key='Hellothere'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/perform')
def perform():
    u=str(request.from['url'])
    n=int(request.form['loop'])
    for i in range(n):
        r()
    return render_template('perform.html')

if __name__ == '__main__':
    app.run(debug=True)