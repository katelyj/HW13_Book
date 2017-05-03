#getting the words from the book
def getwords():
    start = "*** START OF THIS PROJECT GUTENBERG EBOOK BEST RUSSIAN SHORT STORIES ***"
    end = "*** END OF THIS PROJECT GUTENBERG EBOOK BEST RUSSIAN SHORT STORIES ***"
    book = open("book.txt","r").read()
    book = book[book.index(start):book.index(end)]

    lines = book.split("\n")
    words = []
    for line in lines:
	words.extend(line.split(" "))

    words = map(lambda s: s.rstrip('').strip('\",.*').replace('\r',''), words)
    words = filter(lambda w: len(w)>0, words)
    
    return words

#initiate
book = getWords()

#frequency of single word
def freqWord(w):
    l = w.lower()
    return len(filter(lambda s: s.lower() == l, book))

#frequency of two words
def freqTwo(w1,w2):
    return freqWord(w1) + freqWord(w2)

#frequency of group of words
def freqGroup(group):
    if len(group) == 1:
	return freqWord(group[0])
    elif len(group) == 0:
	return 0
    return reduce(freqTwo, group)

def freqHelper(word):
    lw = word.lower()
    return [word.lower(),len(filter(lambda s: s.lower() == lw, book))]

#most frequent word
def mostFreq():
    l = map(freqHelper, book)
    word = ""
    m = 0
    for i in l:
        if i[1] > m:
            m = i[1]
            word = i[0]
    return word
