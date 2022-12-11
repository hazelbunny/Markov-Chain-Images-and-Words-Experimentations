import numpy as np
from random import choice

with open("ao.txt",mode='r', encoding='utf8') as inp:
    raw = inp.read()

corpus = raw.strip().split()

honorifics = ("Mr", "Mrs", "Ms")


def makeSentance(firstWord):
    sentance = []
    sentance.append(firstWord)
    while sentance[len(sentance)-1] != ".":
        sentance.append(choice(main[sentance[len(sentance)-1]]))
    return sentance


main = {}

i=0
while i < len(corpus)-2:
    ending=False
    word=corpus[i]
    nextword=corpus[i+1]
    if word.isupper() or nextword.isupper():
        pass
    else:
        for b in ("\"","\â\€\”","\(","\)","\""):
            word = word.replace(b,"")
            nextword = nextword.replace(b,"")
        for h  in honorifics:
            if h in word:
                dots_allowed=True
            else:
                dots_allowed=False
        if word.endswith((".","?","!")) and not dots_allowed:
            endchar = word[len(word)-1]
            word=word[0:len(word)-1]
            ending = True
        if nextword.endswith((".","?","!")):
            nextword=nextword[0:len(nextword)-1]
        if word != "":
            if word in main.keys():
                if ending == False:
                    main[word].append(nextword)
                else:
                    main[word].append(endchar)
            else:
                if ending == False:
                    main[word]=[nextword]
                else:
                    main[word]=[endchar]
    i=i+1


start = []
for word in main.keys():
    if word[0].isupper():
            for i in main[word]:
                start.append(word)
paragraph = []
while len(paragraph)< 5:
    paragraph.append(makeSentance(choice(start)))

def printArray(paragraph):
    for sentance in paragraph:
        for word in sentance:
            if not word.startswith("."):
                print(" ",end="")
            print(word, end="")
        
printArray(paragraph)
