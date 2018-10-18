# remove punctuations! basic text processing
# to do : remove the [num] found in wikipedia pages.

import nltk, re, pprint
import sys, glob, os
from imp import reload
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import sys
reload(sys)


class preprocess:
    def __init__(self):
        from nltk.corpus import stopwords
        self.swords = set(stopwords.words('english'))
        print(len(self.swords), "stopwords present!")

    def allfiles(self, foldername):  # returns the name of all files inside the source folder.
        owd = os.getcwd()
        fld = foldername + "/"
        os.chdir(fld)  # this is the name of the folder from which the file names are returned.
        arr = []  # empty array, the names of files are appended to this array, and returned.
        for file in glob.glob("*.txt"):
            arr.append(file)
        os.chdir(owd)
        print("All filenames extracted!")
        return arr

    def rem_stop(self, fname, ofilename):
        rawlines = open(fname,'r+', encoding="utf-8").readlines()
        lenl = len(rawlines)
        of = open(ofilename,'w+', encoding="utf-8")
        stemmer = PorterStemmer()
        items_to_clean = set(
            list(stopwords.words('english')) + ['\n', '\n\n', '\n\n\n', '\n\n\n\n'])
        # Items to clean
        regex_non_alphanumeric = re.compile('[^0-9a-zA-Z]')  # REGEX for non alphanumeric chars
        for index, line in enumerate(rawlines):
            cleaned_line=""
            for item in line.split(" ") :
                print("item "+item)
                item = regex_non_alphanumeric.sub('', item)  # Filter text, remove non alphanumeric chars
                item = item.lower()  # Lowercase the text
                item = stemmer.stem(item)  # Stem the text
                if len(item) < 3 and item in items_to_clean:  # If the length of item is lower than 3, remove item
                    item = ''
            cleaned_line+=item
            rawlines[index] = cleaned_line  # Put item back to the list
        cleaned_list = [elem for elem in rawlines if elem not in ['\n', '\n\n', '\n\n\n', '\n\n\n\n'] ]
            # self.drawProgressBar(prog)
        for line in cleaned_list:
            of.write(line)
            of.write("\n")

    def drawProgressBar(self, percent, barLen=50):  # just a progress bar so that you dont lose patience
        sys.stdout.write("\r")
        progress = ""
        for i in range(barLen):
            if i < int(barLen * percent):
                progress += "="
            else:
                progress += " "
        sys.stdout.write("[ %s ] %.2f%%" % (progress, percent * 100))
        sys.stdout.flush()

    def allremove(self):
        array1 = self.allfiles('data')  # give the name of the folder which files you want to import!!
        lenv = len(array1)
        for k in range(lenv):
            progr = (k + 1) / lenv
            in1 = 'data/' + array1[k]
            out1 = 'data_preprocessed/' + array1[k]  # foldername of the output folder, create the folder first, if does not exist
            self.rem_stop(in1, out1)
            self.drawProgressBar(progr)
        print("\nAll files done!")


if __name__ == '__main__':
    rp = preprocess()
    rp.allremove()