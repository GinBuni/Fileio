'''
Created on Feb 3, 2018

@author: ITAUser
'''

filename = "constituton.txt"
numberfile=open("constituton.txt", "r+");

numberwords = 0;

for line in numberfile:
    words = line.split();
    numberwords = numberwords + len(words);
    
print(numberwords);