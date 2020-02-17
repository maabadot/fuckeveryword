# import random

outputFile = open('output.txt', 'w')
inputFile = open('hagen-orf.txt', 'r').read()
lines = inputFile.splitlines()
for i in range(len(lines)):
    if lines[i] == " ":  # between words check
        if lines[i+4] != " ":  # accusative pick
            if lines[i+4][0:2] == "  ":  # not empty check
                outputFile.write("нахуй " + lines[i+4][2:-1].split(" ")[0].replace("*", "") + "\n")  # configure line
            else:
                outputFile.write("нахуй " + lines[i+4].split(" ")[0].replace("*", "") + "\n")  # configure line


# inputFile = open('output.txt', 'r').read() # random picker
# lines = inputFile.splitlines()
# for i in range(0, 2000):
#     rnd = random.randint(0, 65000)
#     if len(lines[rnd]) == 12:
#         print(lines[rnd].upper())
