banList = ["ислам", "христиан", "кавказ", "дагестан", "армян", "чечен"]

outputFile = open('outputSubjective.txt', 'w')
inputFile = open('hagen-orf.txt', 'r').read()
lines = inputFile.splitlines()
for i in range(len(lines)):
    flag = True
    if lines[i] == " ":  # between words check
        if lines[i+1] != " ":  # accusative pick
            for j in range(0, len(banList)):
                if banList[j] in lines[i+1]:
                    flag = False
            if flag:
                line = lines[i+1].split(" ")[0] + "\n"  # configure line
                outputFile.write(line)  # write line

