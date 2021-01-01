import sys

tmp = sys.argv[1:]
a=[]

f=open(tmp[0],'r')
for line in f:
    a.append(line)
f.close()

f=open(tmp[1],'w')

for i in a:
    data= i
    f.write(data)
f.close()
    