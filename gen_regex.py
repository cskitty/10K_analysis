import tokenize

infile = open('dict.txt', 'r')
outfile = open('regex.txt', 'w')
Lines = infile.readlines()

wordlist = []

outfile.write('regexes = [\n')

# Strips the newline character
for line in Lines:
    words = line.strip().split(',')
    for n in words:
        patternWords = n.strip()
        wordList = patternWords.split()
        regExStr = "\\\\b"
        for i in range(len(wordList)):
            w = wordList[i]
            if w.endswith('*'):
                regExStr = regExStr + w[0:-1]
                regExStr = regExStr + "\w*"
            else:
                regExStr = regExStr + w
            if i != len(wordList) -1:
                regExStr = regExStr + "\s+"
        regExStr = regExStr + "\\\\b"
        outfile.write('\t"' + regExStr + '",\n')

outfile.write('\t]\n')
infile.close()
outfile.close()


