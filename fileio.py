'''
Created on Feb 3, 2018

@author: ITAUser
'''
f = open("poem.txt", "r")
#print(f.read())
print(f.readline())
text = f.read()
Words = text.split()
print(Words)
print(len(Words))
#f.close
#f.read(())

fw = open("new.txt", "w")
fw.write("pinnapple goes on pizza")
