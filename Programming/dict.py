f=open("/mnt/DCC8AA9EC8AA7704/Users/Orr/Dropbox/rosalind/dict_example",'r')
text=f.readlines()[0].split()
d={}
for t in text:
    d[t]=0

for t in text:
    d[t]=d[t]+1

for key, value in d.items():
    print key + " " + str(value)
