f=open("/mnt/DCC8AA9EC8AA7704/Users/Orr/Dropbox/rosalind/IO_example",'r')
text=f.readlines()
for i in range(1,len(text),2):
    print text[i]
