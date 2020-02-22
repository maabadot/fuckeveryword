import json
import requests

with open('translate.json', 'r') as configFile:  # config load
    config = configFile.read()
obj = json.loads(config)
yandex_key = str(obj['yandex_key'])

with open('outputSubjective.txt', 'r', encoding="UTF-8") as inputFile:
    lines = inputFile.read().splitlines()
string = ""

outputFile = open('outputYandexTranslate.txt', 'w', encoding="UTF-8")

count = 0
start = 0
end = 100
for j in range(0, 657):
    for i in range(start, end):
        string = string + lines[i] + "\n"
    req_str = "https://translate.yandex.net/api/v1.5/tr/translate?key=" + yandex_key + "&text=" + string + "&lang=ru-en"
    response = requests.post(req_str)
    body = response.content.decode("UTF-8")[82: -21].replace("the ", "")
    outputFile.write(body)
    start += 100
    end += 100
    string = ""
    count += 1
    print("Iteration " + str(count))

# req_google = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&dt=t&dt=bd&dj=1&text={{" + string + "}}t&tl=en"
# response = requests.get(req_google)
# body = response.content.decode("UTF-8")

