from flask import Flask, request
import requests


app = Flask(__name__)

# global variables
#bot_token = '1698251305:AAGG1NVz_gdtTU1EvLGqpZniLyWjg-k_vSc'
bot_token = '5763664452:AAFq9yH8hmMJVkaMIICaEQ3MOvbcNqSPTGA'
global_chat_id = '593444341'
#channel_id = '-1001300825950'
channel_id = '-1001853889313'
threshold = 30000

@app.route ('/')
def welcome():
    return "Hello, Welcome there! This is the Ahmad telegram bot {}".format("\U0001F60A")

@app.route('/webhook', methods=['POST'])
def webhook():
    #decode the byte object.
    data_to_be_logged = request.data.decode('utf-8')
    try:
        print("request body - {}".format(data_to_be_logged))
    except Exception:
        fully_string = data_to_be_logged.replace("'", '"')
        print("request body - {}".format(fully_string))

    print("Sending message to Telegram Channel")
    
    try:
        send_message(chat_id=channel_id, msg=data_to_be_logged)
        message = {"status": 200, "message": "Message sent to telegram successfully"}
    except Exception as e:
        print(e)
        message = {"status": 400, "message": "Could not send message to telegram"}
        return e
        
        
    return message

# fn to send_message through telegram
def send_message(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"

    # send the msg
    requests.get(url)
