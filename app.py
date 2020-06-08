from flask import Flask, render_template, url_for, request, session, redirect, g, jsonify
from selenium import webdriver
import os
import threading
from fake_useragent import UserAgent
ua = UserAgent()
usrand=ua.random
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
def r1(u,n,usrand):
    for i in range(n):
        r(u,usrand)
def r(a,usrand):
    chrome_options.add_argument("user-agent="+usrand)
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(a)
    print(driver.title)
    print driver.page_source.encode("utf-8")
    driver.close()
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
    ua = UserAgent()
    usrand=str(ua.random)
    u=str(session.get('url'))
    u='https://'+u
    n=int(session.get('loop'))
    print(u+'  '+str(n))
    t1 = threading.Thread(target=r1, args=(u,n,usrand,))
    t1.start()
    return render_template('perform.html')

if __name__ == '__main__':
    app.run(debug=True)