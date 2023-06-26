import os
import random
import telegram
import schedule
import time

bot = telegram.Bot(token='YOUR_BOT_TOKEN')
channel_id = 'YOUR_CHANNEL_ID'

# read applers
def read_from_file(file_to_read: str='applers.txt', mode: str()='r',
                   return_as: str='list') -> str:
    try:
        current_file_path = os.path.join(os.getcwd(), file_to_read)
        with open(current_file_path, mode) as f:
            # Read the contents of the file
            file_content = f.read()
            if return_as == 'list':
                return file_content.splitlines()
        return file_content
    except Exception as e:
        print(e)

# shuffle applers
def shuffle_applers(applers: list) -> str():
    return random.choice(applers)

# post appler to telegram
def job():
    applers = read_from_file('applers.txt')
    print(f'Todays appler candidates are:{applers}\ntype: {type(applers)}')

    appler = shuffle_applers(applers)
    print(f'appler is: {appler}\ntype: {type(appler)}')
    
    bot.send_message(chat_id=channel_id, text=f'{appler} is today appler.')

def post_appler_to_telegram():
    schedule.every().day.at("21:41").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

post_appler_to_telegram()