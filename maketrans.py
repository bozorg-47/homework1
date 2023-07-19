myDict = {"F":"C","l":"b",",":"!"}
table = str.maketrans(myDict)
text = "hello,yusof"
print(text.translate(table))