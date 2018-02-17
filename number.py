'''
Created on Feb 3, 2018

@author: ITAUser
'''

filename = "number.txt"
numberfile=open(filename, "r+");

numberline = 0;
numberwords = 0;
numberchar = 0;

for line in numberfile:
    words = line.split();
    
    numberline = numberline +1;
    numberwords = len(words);
    numberchar = len(line);
    
print(numberchar);