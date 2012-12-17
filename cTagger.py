## cTagger Comma-placing script v1.0 alpha (2012) ##
## --- Description ---                            ##

import os
import re
import sys

"""importText
Opens the file specified by the user using the 'rU' flag. Returns a FileNotFounderror
if the file is not found.
"""
def importText(location):
    f = open(location,'rU');
    text = f.read();
    # print text;     - debug
    f.close();

    # Use a regular expression matching a full-stop not preceded by an integer (numeric)
    # to split the text into full sentences.
    
    

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