_string = "ThiS is String with Upper and lower case Letters"
s=_string.lower()
word={}
for i in s:
    word[i]=word.get(i,0)+1
items=list(word.items())
items.sort()
del items[0]
print(items)
for i,j in items:
    print(i,j)