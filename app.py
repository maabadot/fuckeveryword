import requests
import json
import time

with open('config.json', 'r') as configFile:  # config load
    config = configFile.read()
obj = json.loads(config)
owner_id = str(obj['owner_id'])
vk_token = str(obj['vk_token'])
tg_token = str(obj['tg_token'])

while True:
    with open('dictionary.txt', 'r', encoding="utf-8") as fin:  # pick first line
        line = fin.readline()
        data = fin.read().splitlines(True)
    with open('dictionary.txt', 'w', encoding="utf-8") as fout:  # delete first line
        fout.writelines(data[0:])
    vk_request = "https://api.vk.com/method/wall.post?owner_id=" + owner_id + "&message=" + line +"&access_token=" + vk_token + "&v=5.103"  # configure VK request
    tg_request = "https://api.telegram.org/bot" + tg_token + "/sendMessage?chat_id=@fuckeveryword&text=" + line  # configure TG request
    requests.get(vk_request)  # VK request
    requests.get(tg_request)  # TG request
    print("Line posted: " + line)
    time.sleep(1730)  # 28 minutes 50 seconds; 49 posts a day



