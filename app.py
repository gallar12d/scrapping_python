
from flask import Flask
from flask_restful import Resource, Api
import os
import time
import selenium
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM

app = Flask(__name__)
api = Api(app)
# Complete these 2 fields ==================
USERNAME = 'gallargod12'
PASSWORD = 'gallardodiego12'
TIMEOUT = 15


class HelloWorld(Resource):

    def get(self, username):
        usr = username

        # user_input = int(
        #     input('How many followers do you want to scrape (60-500 recommended): '))

        options = webdriver.ChromeOptions()
        
        options = webdriver.ChromeOptions()
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        # options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument("--log-level=3")

        bot = webdriver.Chrome(executable_path=CM().install(), options=options)

        bot.get('https://www.instagram.com/accounts/login/')

        time.sleep(2)

        # print("Logging in...")

        user_element = WebDriverWait(bot, TIMEOUT).until(
            EC.presence_of_element_located((
                By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))

        user_element.send_keys(USERNAME)

        pass_element = WebDriverWait(bot, TIMEOUT).until(
            EC.presence_of_element_located((
                By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))

        pass_element.send_keys(PASSWORD)

        login_button = WebDriverWait(bot, TIMEOUT).until(
            EC.presence_of_element_located((
                By.XPATH, '//*[@id="loginForm"]/div/div[3]')))

        time.sleep(0.4)

        login_button.click()

        time.sleep(5)

        bot.get('https://www.instagram.com/{}/?_a=1'.format(usr))

        time.sleep(3.5)

        count = WebDriverWait(bot, TIMEOUT).until(
            EC.presence_of_element_located((
                By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span'))).text

        time.sleep(2)

        return {'count': count}


# api.add_resource(HelloWorld, '/')
api.add_resource(HelloWorld, '/<string:username>')


if __name__ == '__main__':
    app.run()
