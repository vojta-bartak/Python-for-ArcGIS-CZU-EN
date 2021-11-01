def sort(listt):
    for i in range(len(listt)-1):
        if  listt[i]<listt[i+1]:
            listt[i+1],listt[i]=listt[i],listt[i+1]
            return(listt)
