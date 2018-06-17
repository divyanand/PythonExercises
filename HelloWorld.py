import math
from math import sqrt as Sqrt
from urllib.request import urlopen

print ("Hello world 123")

print ("Let us start with import statement with an example of importing math library")
print ("Before we start, let us make sure we have \"import math\" at the top")
print ("Now, lets find square root of few variables using different forms")
print ("math.sqrt(81) =", math.sqrt(81))
print ()
print ("But, if we use \"from math import sqrt as Sqrt\", \
we can use, Sqrt(169) =", Sqrt(169))
print ()
print ()
print ("Let us see some numbers")
print ("0b10 =", 0b10,"0o10 =", 0o10, "0x10 =", 0x10)
print ("int(3.5) =", int(3.5))
print ("int(\"454\") =", int("454"))
print ()
print ()
print ("Bool")
g = 'g'
print (g == 'g')

if True:
    print ("It's true")

if False:
    print ("It's false")
else :
    print ("Apparantly, it is not False")


c = 5
while c <= 10:
    print (c)
    if c == 9 :
        print ("Breaking since c is 9")
        break
    c += 1

for i in range(10):
    print (i)

print ()
print ()
print ("strings and collections")

name = "divyanand"
print (name)
print (name.capitalize())
print (name.split('a'))
print (name.split('a').__len__())
print (name.title())
print ("Casefold comparistion is", "DiVyanAnd".casefold() == name.casefold())
print (name.center(2))
print (name.center(9))
print (name.count("a"))
print (name.endswith("d"))
print (name.upper())
print (name.lower())
print (name.__add__(" rangu"))

a = 5
print (a)
b = a
print (b, id(b), id(a), id(5))

a = 10
print (b, id(b), id(a), id(5), id(10))

c = 10
print(c, id(c))

def fetch_word():
    with urlopen("http://sixty-north.com/c/t.txt") as story:
        story_words = []
        for line in story:
            line_words = line.decode("utf-8").split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_words(story_words):
    for word in story_words:
        print(word)

def main1():
    words = fetch_word()
    print_words(words)


