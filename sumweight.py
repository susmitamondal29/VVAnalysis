for sub in ['zz','jj','']:
    flist=open("event_counts"+sub+".txt")
    weightsum=0
    eventcount=0

    for line in flist:
        num = float(line)
        weightsum+=num
        if num==1:
            eventcount+=1

    print(sub+'sum and event count are: %s %s'%(weightsum,eventcount))
    flist.close()
