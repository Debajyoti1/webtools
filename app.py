from flask import Flask, render_template, url_for, request, session, redirect, g, jsonify
from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
global driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
def r(a):
    driver.get(a)
    print(driver.title)
app = Flask(__name__)
app.secret_key='Hellothere'
@app.route('/',methods=['GET','POST'])
def index():
    session.pop('u',None)
    session.pop('n',None)
    if request.method == 'POST':
        u= request.form['url']
        p=request.form['loop']
        session['url']=u
        session['loop']=p
        return redirect(url_for('perform'))
    return render_template('index.html')
@app.route('/perform',methods=['GET','POST'])
def perform():
    u=str(session.get('url'))
    u='https://'+u
    n=int(session.get('loop'))
    print(u+'  '+str(n))
    for i in range(n):
        r(u)
    return render_template('perform.html')

if __name__ == '__main__':
    app.run(debug=True)