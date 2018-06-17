'''
Created on Jun 17, 2018

@author: H122817
'''

"""This one will compare all the files in a given dir, ending with a given patter of file name and reports the duplicates"""
"""Usage : CompareFiles.py <directory path> <pattern with which the filename ends>"""

import os.path
import sys
from operator import itemgetter
from filecmp import cmp

if __name__ == '__main__':

    DirPath = str()
    fileEnding = str()
    if len(sys.argv) > 2:
        DirPath = sys.argv[1]
        fileEnding = sys.argv[2]
    else :
        DirPath = input("Enter directory to search for files:")
        fileEnding = input("Enter pattern for filename ending:")

    #DirPath = "C:\\SVN_Repositories\\STTNG\\testcases\\zsim\\customer\\203" #input ("Enter folder path :")
    #fileEnding ="_1_Fiji_ref.png"

    try: 
        #list down the files and get their sizes
        filelist = list()
        for filename in os.listdir(path=DirPath):
            if filename.endswith(fileEnding):
                filePath = DirPath + "\\" + filename
                filestat = os.stat(filePath)
                filedetails = list((filestat.st_size, filename, filePath))
                filelist.append(filedetails)
        #now sort them based on their size
        filelist.sort(key=itemgetter(0))

#        for file in filelist:
#            print(file) 
        print (len(filelist))

        #Now compare the contents if the file size is same
        #iterate through all the files till files are left in the list
        filelistBackup = list()
        while len(filelist) > 1:
            removelist = list()
            removelist.append(0)

            for counter in range(1, len(filelist)):
                if(filelist[0][0] >= filelist[counter][0]):
                    # we got two file with same file size. See if the contents are both same
                    #print(filelist[0], filelist[counter])
                    try:
                        if cmp(filelist[0][2], filelist[counter][2], shallow=False):
                            print(filelist[0][1], "\t<== Matches with ==>\t", filelist[counter][1])
                    except FileNotFoundError:
                        print("Unable to open file",filelist[counter][1])
                    removelist.append(counter)
                else :
                    break;
                
            removelist.reverse()
            for index in removelist:
                filelistBackup.append(filelist.pop(index))
                
    except FileNotFoundError:
        print ("Unable to open file")

    print("End of routien")
