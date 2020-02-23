import requests
import json

with open('outputSubjective.txt', 'r', encoding="UTF-8") as inputFile:
    lines = inputFile.read().splitlines()
string = ""

outputFile = open('outputGoogleTranslate.txt', 'a', encoding="UTF-8")

for j in range(584, 657):
    for i in range(j * 100, j * 100 + 100):
        string = string + lines[i] + "\n"

    req_str = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&dt=t&dt=bd&dj=1&text={{" + string + "}}t&tl=en"
    response = requests.post(req_str)
    # print(response.content)
    body = json.loads(response.content.decode("UTF-8"))
    for i in range(len(body["sentences"]) - 1):
        if i == 0:
            outputFile.write(body["sentences"][i]["trans"][2:])
        else:
            outputFile.write(body["sentences"][i]["trans"])
    string = ""
    print("Iteration " + str(j))

