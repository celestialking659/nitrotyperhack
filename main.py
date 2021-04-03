from flask import Flask, request
from bot import startbots, stopbot
import threading
import codecs, time
import requests
from bot import racer
app = Flask(__name__)
@app.route('/', methods=['HEAD', 'GET'])
def main():
    file = codecs.open("main.html", "r", "utf-8")
    return file.read()
@app.route('/start', methods=['POST'])
def start():
    def post():
        requests.post('https://test.ntrodeveloper.repl.co/botstart')
    thread = threading.Thread(target=post)
    thread.start()
    thread.join(2)
    return 'startedbot'
@app.route('/stop', methods=['POST'])
def stop():
    stopbot()
    return 'stopped!'
@app.route('/botstart', methods=['POST'])
def startbot():
    startbots()
def automate():
    time.sleep(3)
    while True:
        requests.post('https://test.ntrodeveloper.repl.co/start')
        print('done')
        time.sleep(300)
@app.route('/otherstart', methods=['POST'])
def otherstart():
    form = request.form
    username = form['username']
    password = form['password']
    speed = int(form['speed'])
    accuracy = int(form['accuracy'])
    global bot
    bot = racer(username, password, speed, accuracy, 100000, 'true') 
    thread = threading.Thread(target=bot.startBot())
    thread.start()
    thread.join(3)
    return 'started bot'
@app.route('/otherstop', methods=['POST'])
def otherstop():
    bot.stopBot()
    return 'stopped!'
def run():
    app.run(host="0.0.0.0", port=8080)
mainthread = threading.Thread(target=run)
auto = threading.Thread(target=automate)
mainthread.start()
auto.start()
mainthread.join()
