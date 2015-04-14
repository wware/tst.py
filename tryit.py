import ctypes
import os
import re
import time
import urllib2


## Build the C code and import it using ctypes.
os.system("gcc -g -shared -DLIB=1 -o libtst.so tst.c")
tst = ctypes.cdll.LoadLibrary("./libtst.so")


def search_gutenberg_text(name, url):
    t1 = time.time()
    text = urllib2.urlopen(url).read()
    t2 = time.time()
    [tst.insert(word) for word in re.split("\W+", text)]
    t3 = time.time()
    for word in ("cats", "galactic", "whale", "parsec", "Valjean", "Sobriquet"):
        print "The word \"{0}\" {1} in the text of {2}.".format(
            word,
            tst.search(word) and "is" or "is NOT",
            name
        )
    t4 = time.time()
    print "{0} seconds to build the tree\n{1} seconds of searching\n".format(
        # t2 - t1,    I don't care about the slow HTTP GET
        t3 - t2,
        t4 - t3
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
