f1r = open('outputFinalText.txt', 'r').read()
f1w = open('outputFinalText.txt', 'w')
lines1 = f1r.splitlines()

f2r = open('outputGoogleTranslate.txt', 'r').read()
f2w = open('outputGoogleTranslate.txt', 'w')
lines2 = f2r.splitlines()

f3r = open('outputYandexTranslate.txt', 'r').read()
f3w = open('outputYandexTranslate.txt', 'w')
lines3 = f3r.splitlines()

f4r = open('outputSubjective.txt', 'r').read()
f4w = open('outputSubjective.txt', 'w')
lines4 = f4r.splitlines()

for i in range(0, 65000):
    if lines1[i] == lines1[i+1]:
        lines1.pop(i)
        lines2.pop(i)
        lines3.pop(i)
        lines4.pop(i)

length = len(lines1)
for i in range(length):
    f1w.write(lines1[i] + '\n')
    f2w.write(lines2[i] + '\n')
    f3w.write(lines3[i] + '\n')
    f4w.write(lines4[i] + '\n')
