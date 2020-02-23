banList = ["ислам", "христиан", "кавказ", "дагестан", "армян", "чечен"]

outputFile = open('outputFinalText.txt', 'w')
inputFile = open('hagen-orf.txt', 'r').read()
lines = inputFile.splitlines()
linesCopy = []
for i in range(len(lines)):
    flag = True
    if lines[i] == " ":  # between words check
        if lines[i+2] == " ":
            for j in range(0, len(banList)):
                if banList[j] in lines[i+4]:
                    flag = False
            if flag:
                line = "нахуй " + lines[i+1].split(" ")[0] + "\n"  # configure line
                outputFile.write(line)  # write line
        elif lines[i+4] != " ":  # accusative pick
            for j in range(0, len(banList)):
                if banList[j] in lines[i+4]:
                    flag = False
            if flag:
                if lines[i+4][0:2] == "  ":  # not empty check
                    line = "нахуй " + lines[i+4][2:-1].split(" ")[0].replace("*", "") + "\n"  # configure line
                    outputFile.write(line)  # write line
                else:
                    line = "нахуй " + lines[i+4].split(" ")[0].replace("*", "") + "\n"  # configure line
                    outputFile.write(line)  # write line
        else:
            for j in range(0, len(banList)):
                if banList[j] in lines[i+4]:
                    flag = False
            if flag:
                line = "нахуй " + lines[i+1].split(" ")[0] + "\n"  # configure line
                outputFile.write(line)  # write line
