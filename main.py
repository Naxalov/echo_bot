#Import library for telegram bot
import requests

TOKEN = '5446020024:AAHcDq0gInuUnVWolbamoUNoqbFA490U4N8'

#Send message 
def send_message(text:str, chat_id:int):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    answer = requests.post(url, data={'chat_id': chat_id, 'text': text})
    return answer.json()


#Get updates
def get_updates():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    answer = requests.get(url)
    data = answer.json()
    # Get result form data
    result = data['result']    
    
    return result

def get_last_update(updates):
    # Get last update
    update = updates[-1]
    # Get message text
    text = update['message']['text']
    # Get chat id
    chat_id = update['message']['chat']['id']
    # Get update id
    update_id = update['update_id']
    return text, chat_id,update_id


# Last update id
last_update_id = get_last_update(get_updates())[-1]
#Send message through loop
current_update_id = -1 #results[-1]['update_id']
while True:
    results = get_updates()

    text, chat_id ,current_update_id = get_last_update(results)
    if last_update_id != current_update_id:
        print(last_update_id)
        send_message(text, chat_id)
        
        last_update_id = current_update_id

    

# chat_id = '5575549228'
# idx = 1
# while True:
#     #Send message to chat_id
#     send_message(f'Hello: {idx}', chat_id)
#     idx+=1
#     print(f'Message sent:{idx}')