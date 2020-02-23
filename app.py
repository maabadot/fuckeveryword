import requests
import json
import time
import vk
import telebot

with open('config.json', 'r') as configFile:  # config load
    config = configFile.read()
obj = json.loads(config)
owner_id = str(obj['owner_id'])
vk_token = str(obj['vk_token'])
tg_token = str(obj['tg_token'])
unsplash_token = str(obj['unsplash_token'])

session = vk.Session(access_token=vk_token)
vk_api = vk.API(session)

telegram_bot = telebot.TeleBot(tg_token)


def find_url(query1, query2):
    unsplash_request1 = 'https://api.unsplash.com/search/photos?client_id=' + unsplash_token + '&query=' + query1 + '&per_page=20'
    unsplash_response1 = requests.get(unsplash_request1)
    body1 = json.loads(unsplash_response1.content.decode('UTF-8'))

    unsplash_request2 = 'https://api.unsplash.com/search/photos?client_id=' + unsplash_token + '&query=' + query2 + '&per_page=20'
    unsplash_response2 = requests.get(unsplash_request2)
    body2 = json.loads(unsplash_response2.content.decode('UTF-8'))

    if body1['total'] != 0:
        with open('links.txt', 'r') as file:
            links = file.read().splitlines()
        for i in range(len(body1['results'])):
            if body1['results'][i]['urls']['regular'] not in links:
                with open('links.txt', 'a') as file:
                    file.write(body1['results'][i]['urls']['regular'] + '\n')
                return body1['results'][i]['urls']['regular']
        return 'None'
    elif body2['total'] != 0:
        with open('links.txt', 'r') as file:
            links = file.read().splitlines()
        for i in range(len(body2['results'])):
            if body2['results'][i]['urls']['regular'] not in links:
                with open('links.txt', 'a') as file:
                    file.write(body2['results'][i]['urls']['regular'] + '\n')
                return body2['results'][i]['urls']['regular']
        return 'None'
    else:
        return 'None'


def post_vk(line, img_url):
    if img_url == 'None':
        vk_api.wall.post(owner_id=owner_id, message=line, v=5.103)
    else:
        image = requests.get(img_url, stream=True)
        destination = vk_api.photos.getWallUploadServer(group_id=owner_id[1:], v=5.103)
        data = ('image.jpg', image.raw, image.headers['Content-Type'])
        meta = requests.post(destination['upload_url'], files={'photo': data}).json()
        photo = vk_api.photos.saveWallPhoto(group_id=owner_id[1:], server=meta['server'], photo=meta['photo'], hash=meta['hash'], v=5.103)[0]
        vk_api.wall.post(owner_id=owner_id, message=line, attachments='photo' + str(photo['owner_id']) + '_' + str(photo['id']), v=5.103)


def post_tg(line, img_url):
    if img_url == 'None':
        telegram_bot.send_message(chat_id='@fuckeveryword', text=line)
    else:
        image = requests.get(img_url, stream=True)
        with open('image.jpg', 'wb') as f:
            for chunk in image:
                f.write(chunk)
        telegram_bot.send_photo(chat_id='@fuckeveryword', photo=open('image.jpg', 'rb'), caption=line)


def pick_line():
    with open('dictionary.txt', 'r', encoding="utf-8-sig") as file1_r:  # pick first line
        line1 = file1_r.readline()
        data = file1_r.read().splitlines(True)
    with open('dictionary.txt', 'w', encoding="utf-8") as file1_w:  # delete first line
        file1_w.writelines(data[0:])

    with open('dictionaryTranslateG.txt', 'r', encoding="utf-8-sig") as file2_r:  # pick first line
        line2 = file2_r.readline()
        data = file2_r.read().splitlines(True)
    with open('dictionaryTranslateG.txt', 'w', encoding="utf-8") as file2_w:  # delete first line
        file2_w.writelines(data[0:])

    with open('dictionaryTranslateY.txt', 'r', encoding="utf-8-sig") as file3_r:  # pick first line
        line3 = file3_r.readline()
        data = file3_r.read().splitlines(True)
    with open('dictionaryTranslateY.txt', 'w', encoding="utf-8") as file3_w:  # delete first line
        file3_w.writelines(data[0:])

    return [line1, line2, line3]


while True:
    line = pick_line()
    print(line)
    url = find_url(query1=line[1][:-1], query2=line[2][:-1])
    post_vk(line=line[0][:-1], img_url=url)
    post_tg(line=line[0][:-1], img_url=url)

    print("Line posted: " + line[0][:-1] + ' / ' + line[1][:-1] + ' / ' + line[2][:-1])
    print("Image: " + url)
    time.sleep(1680)  # 28 minutes; 49 posts a day
