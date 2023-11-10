from flask import Flask, request
from bot import ZdgBot

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        zdgBot = ZdgBot(request.json)
        return zdgBot.processRreceivedMessage()

if(__name__) == '__main__':
    app.run()