words = list(map(str,input("Enter Strings:").split()))
print(words)
common= list()
for char in words[0]:
    if all(char in word for word in words):
        if all(max(word.count(char) for word in words )):
            common.append(char)
print(common)

