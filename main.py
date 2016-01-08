__author__ = 'BlackSwan'


import sys, os
from random import randint
import shutil

if len(sys.argv) > 0:
    print "File name: " + sys.argv[1]
    file = sys.argv[1]
    basename, ext = file.split(".")

    print ext
    exts = []
    indices = set([randint(0,len(ext)-1)])

    exts.append("".join(c.upper() if i in indices else c for i, c in enumerate(ext)))

    if ext == "php":
        exts.append("php5")
        exts.append("php3")
        exts.append(exts[0] + "3")
        exts.append(exts[0] + "5")

    exts.append(ext + " ")
    exts.append(ext + ".")
    exts.append(ext + " ... ... . . .. ..")
    null = "\x00"
    #trying to find a way to insert null, but you need to do it with a proxy
    #exts.append(ext + null + ".jpg")

    if ext == "html" :
        exts.append("shtml")

    exts.append(ext + ";.jpg")
    exts.append(ext + ".jpg")
    counter = 0


    for j in exts:
        print j
        try:
            os.makedirs("basename"+str(counter)+"/")
        except:
            pass
        try:
            shutil.copy(file, "basename"+str(counter)+"/")
            os.chdir("basename"+str(counter)+"/")
            os.rename(file, "basename"+"."+j)
            os.chdir("..")
            counter += 1
        except ValueError as e:
            print "Oops! Something went wrong."
            print e

else:
    print "The name of the file is missing as an argument"
