import os
import re

def scandir(startdir, target) :
    os.chdir(startdir)
    for obj in os.listdir(os.curdir) :
        #if obj == target :
            #print os.getcwd() + os.sep + obj
    
        
        if os.path.isdir(obj) :        
            scandir(obj, target)
            os.chdir(os.pardir) #!!!
        else:
            myfile = open(obj,"r")
            linenum = 1
            while True:
                line = myfile.readline()
                if not line:
                    break
                li = line.find(target)
                if li !=  -1:
                    print os.getcwd() + os.sep + obj + '----' + str(linenum)
                linenum = linenum+1
            #print os.getcwd() + os.sep + obj
            myfile.close()
print('usage --  /dir you traval and string you wanna search/')
startdir = raw_input('Please input startdir: ')
target = raw_input('Please input target: ')
scandir(startdir, target)
