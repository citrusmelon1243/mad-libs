import re

#The document must be set to a doc that is intended for mad libs, i.e. a document that has certain words with
# double underscores and a part of speech

doc = open("/home/curtisbyers/madlib.txt", "r")
texts = doc.read()
def mad_libs(text):

    words = (re.findall("__.*?__", text, re.MULTILINE))

    for word in words:
        q = "Enter a {}".format(word)
        new = input(q)
        text = text.replace(word, new, 1)
    print(text)
mad_libs(texts)






    


