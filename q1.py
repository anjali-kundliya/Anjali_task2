sentence=str(input("Enter a sentence: "))
words=sentence.split()
letters=sum(map(len,words))
words=len(words)
average=letters/words
print(average)
