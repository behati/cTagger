## cTagger Comma-placing script v1.0 alpha (2012) ##
## --- Description ---                            ##

import os
import re
import sys

"""importText
Opens the file specified by the user using the 'rU' flag. Returns an error
if the file is not found.
"""
def importText(location):
    try:
        f = open(location,'rU');       
    except IOError:
        print "Error: The file was not found";
        inputPrompt();
    else:
        text = f.read();
        # print text;      - debug
        f.close();

        # Use a regular expression matching a full-stop not preceded by an integer (numeric)
        # to split the text into full sentences.
        sentences = re.split('\s+([.][/]RESID_SIGN)+',text);

        # Since we've split by the above expression, we add it to each sentence 
        # and remove stand-alones
        tempSen  = filter(lambda x: x != "./RESID_SIGN", sentences);
        finalSen = [];
        for s in tempSen:
            finalSen.append(s + " ./RESID_SIGN");

        # print finalSen;   - debug
        
 
"""SortTags(List)
Takes a list of sentences and cuts each word in the sentence from its' tag, then places
word and tag into a key/value dictionary. Returns a list of dictionaries, each representing
an original sentence 
"""
   
# def SortTags(sentenceList):
            

"""inputPrompt - Prompts the user for terminal input containing the absolute path 
of a readable file, using the raw_input function. 
"""
def inputPrompt():
    filepath = raw_input("File: ");
    importText(filepath);

"""main - starts the script by printing the start-up text and the calling inputPrompt()
"""
def main():
    print ">>> cTagger v1.0 (Dec 2012) - type -help for help and -quit to quit. \n";
    inputPrompt();
if __name__ =='__main__':
    main();

