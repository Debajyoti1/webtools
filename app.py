from flask import Flask, render_template, url_for, request, session, redirect, g
from selenium import webdriver
import os
import threading
from fake_useragent import UserAgent
import time
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
    driver.delete_all_cookies()
    driver.get(a)
    print(driver.title)
    print(driver.get_cookies())
    print(driver.page_source.encode("utf-8"))
    driver.delete_all_cookies()
    driver.close()

def r2(u,usrand):
    chrome_options.add_argument("user-agent="+usrand)
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.delete_all_cookies()
    driver.get(u)
    driver.maximize_window()
    print(driver.title)
    time.sleep(60)
    print(driver.get_cookies())
    driver.delete_all_cookies()

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

@app.route('/performyt',methods=['GET','POST'])
def performyt():
    ua = UserAgent()
    usrand=str(ua.random)
    u=str(session.get('ur'))
    u='https://'+u
    print(u)
    t1 = threading.Thread(target=r2, args=(u,usrand,))
    t1.start()
    return render_template('perform.html')

@app.route('/yt',methods=['GET','POST'])
def yt():
    session.pop('ur',None)
    if request.method == 'POST':
        ur= request.form['ur']
        session['ur']=ur
        return redirect(url_for('performyt'))
    return render_template('yt.html')
if __name__ == '__main__':
    app.run(debug=True)