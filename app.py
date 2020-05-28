from flask import Flask, render_template, url_for, request, session, redirect, g, jsonify
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
import os
CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')
options = Options()
options.binary_location = GOOGLE_CHROME_BIN
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.headless = True
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH , chrome_options=options)

url = 'https://gadgetguys.in'
driver.get(url)
app = Flask(__name__)
app.secret_key='Hellothere'
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)