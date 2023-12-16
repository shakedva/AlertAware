from flask import Flask, Response, request
import requests


TOKEN = '6358416870:AAE3P5xB65cEzWDdAUs2xXqWfNr6Mhz0ckg'
NGROK_URL = 'https://e1cf-82-80-173-170.ngrok-free.app'
CHAT_ID = '5617966555'

TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url={}/message'.format(TOKEN, NGROK_URL)

# Create a Flask app
app = Flask(__name__)


# Create a route that returns a message
@app.route('/sanity')
def sanity():
    return "Server is running"


@app.route('/message', methods=["POST", "GET"])
def handle_message():
    msg = request.form.get('text')
    if msg:
        print(msg)
    else:
        msg = 'got it'
    print(msg)
    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TOKEN, CHAT_ID, msg))
    return Response("success")


if __name__ == '__main__':
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)
    app.run(port=5002)
