import sys

orgin=[]
tmp=[]
f= open('score.txt','r')
for line in f:
    a= line.strip().split(' ')
    orgin.append(a)
    total = (float(a[1])*0.4)+(float(a[2])*0.6)
    if(total>=90):
        tmp.append(str(total)+'(A)')
    elif(total>=80):
        tmp.append(str(total)+'(B)')
    elif(total>=70):
        tmp.append(str(total)+'(C)')
    elif(total>=60):
        tmp.append(str(total)+'(D)')
    elif(total<60):
        tmp.append(str(total)+'(F)')
f.close()


f=open('report.txt','w')
for i in range(len(tmp)):
    orgin[i].extend([tmp[i]+"\n"])
    f.write(" ".join(orgin[i]))
f.close()
    
       
