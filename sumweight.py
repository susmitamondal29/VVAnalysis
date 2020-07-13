import matplotlib.pyplot as plt
import sys,numpy

plotting = False
firstline= True
x=[]

sub=sys.argv[1]
filename=sys.argv[2]
phrase=sys.argv[3] if len(sys.argv)>3 else None 

if not sub in ['16','17','18']:
    print("invalid argument")
    sys.exit(1)

flist=open(filename)
weightsum=0
eventcount=0

for line in flist:
    if firstline and not phrase:
        phrase=line.strip().split(':')[0]+':'
        firstline=False
    if phrase in line:
        line=line.replace(phrase,'')
        num = float(line.strip())
        weightsum+=num
        
        if not line.strip()=='0':
            eventcount+=1
            x.append(num)

mean=numpy.mean(x)
std=numpy.std(x)

print('sum and event count are: %s %s'%(weightsum,eventcount))
print(sorted(x)[:20])
print(sorted(x,reverse=True)[:20])
print('mean:%s std:%s'%(mean,std))
flist.close()

if plotting:
    fig,ax=plt.subplots(figsize=(15,10))
    ax.hist(x,range=(mean-3*std,mean+3*std),bins=20)
    ax.set_title("(SF, L1PrefiringWeight not applied)Weight distribution for 20"+sub)
    ax.set_xlabel("weight")
    ax.set_ylabel("event")
    plt.savefig("NoSFNoPrefiredweight%s.png"%sub)
