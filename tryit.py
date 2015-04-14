import ctypes
import os
import re
import urllib2


## Build the C code and import it using ctypes.
os.system("gcc -g -shared -DLIB=1 -o libtst.so tst.c")
tst = ctypes.cdll.LoadLibrary("./libtst.so")


## Let's look for words in the text of Herman Melville's "Moby Dick".
moby_dick = urllib2.urlopen("https://www.gutenberg.org/files/2701/2701.txt").read()
[tst.insert(word) for word in re.split("\W+", moby_dick)]

for word in ("cats", "galactic", "whale", "parsec"):
    print "The word \"{0}\" {1} in the text of Moby Dick.".format(
        word,
        tst.search(word) and "is" or "is NOT"
    )


## Discard the search tree for Moby Dick to prepare for another text to search.
tst.cleanup()
print


## Carl Vilhelm Ludvig Charlier, "Lectures on Stellar Statistics", Hamburg Germany, 1921
stellar_stats = urllib2.urlopen("https://www.gutenberg.org/files/22157/22157-0.txt").read()
[tst.insert(word) for word in re.split("\W+", stellar_stats)]

for word in ("cats", "galactic", "whale", "parsec"):
    print "The word \"{0}\" {1} in the text of Lectures on Stellar Statistics.".format(
        word,
        tst.search(word) and "is" or "is NOT"
    )
