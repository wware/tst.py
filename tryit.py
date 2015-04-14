import ctypes
import os
import re
import time
import urllib2


## Build the C code and import it using ctypes.
assert os.system("gcc -g -shared -DLIB=1 -o libtst.so tst.c") == 0
tst = ctypes.cdll.LoadLibrary("./libtst.so")


def search_gutenberg_text(name, url):
    text = urllib2.urlopen(url).read()
    t1 = time.time()
    tst.scan(text)
    t2 = time.time()
    for word in ("cats", "galactic", "whale", "parsec", "Valjean", "Sobriquet"):
        print "The word \"{0}\" {1} in the text of {2}.".format(
            word,
            tst.search(word) and "is" or "is NOT",
            name
        )
    t3 = time.time()
    print "{0} seconds to build the tree\n{1} seconds of searching\n".format(
        t2 - t1,
        t3 - t2
    )
    tst.cleanup()


## Herman Melville's "Moby Dick".
search_gutenberg_text(
    "Moby Dick",
    "https://www.gutenberg.org/files/2701/2701.txt"
)

## Victor Hugo, "Les Miserables", a *miserably* long novel.
search_gutenberg_text(
    "Les Miserables",
    "http://www.gutenberg.org/files/135/135.txt"
)

## Carl Vilhelm Ludvig Charlier, "Lectures on Stellar Statistics", Hamburg Germany, 1921
search_gutenberg_text(
    "Lectures on Stellar Statistics",
    "https://www.gutenberg.org/files/22157/22157-0.txt"
)
