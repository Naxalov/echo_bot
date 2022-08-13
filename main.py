#Import library for telegram bot
import requests

TOKEN = '5355192064:AAHeVCobTRAUsm0lsi9e_l_QZbfFMVuVFeM'

#Send message 
def send_message(text:str, chat_id:int):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    answer = requests.post(url, data={'chat_id': chat_id, 'text': text})
    return answer.json()


#Get updates
def get_updates()->list:
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    answer = requests.get(url)
    data = answer.json()
    # Get result form data
    result = data['result']    
    
    return result

def get_last_update(result:list):
    # Get last update
    update = result[-1]
    # Get message text
    text = update['message']['text']
    # Get chat id
    chat_id = update['message']['chat']['id']
    # Get update id
    update_id = update['update_id']
    return text, chat_id,update_id
    
stroge=''

while True:
    result = get_updates()
    text, chat_id, update_id = get_last_update(result)
    print(text, stroge)
    if text != stroge:
        stroge=text
        send_message(text, chat_id)
