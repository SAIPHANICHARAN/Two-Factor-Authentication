b

f=open("collecteddata.txt",'r')
a=f.read()
print(a)
b=a.split(',')
print(b)
for i in range(len(b)-1):
    print(b[i])
