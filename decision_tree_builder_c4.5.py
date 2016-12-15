import math
from collections import defaultdict
from collections import Counter

def mlog(x):
    if x==1.0 or x==0.0:
        return 0
    return -1*x*math.log(x,2)

def maximize(d):
    m=0
    key=''
    for k in d.keys():
       if d[k]>m:
           m=d[k]
           key=k
    if m==0:
        return "No more information gain!!!"
    return key

data=defaultdict(list)

data['day']=range(1,15)
data['outlook']=['Sun','Sun','Overcast','Rain','Rain','Rain','Overcast','Sun',
                 'Sun','Rain','Sun','Overcast','Overcast','Rain']
data['temp']=[26,25,25,24,19,20,20,23,20,25,24,22,23,23]
data['humidity']=['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal','Normal','High','Normal','High']
data['wind']=['Low','High','Low','Low','Low','High','High','Low','Low','Low','High','High','Low','High']
data['play']=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

def best_attribute(dataset):
    n=float(len(dataset['play']))
    p_play_no=float(dataset['play'].count('No'))/n
    p_play_yes=float(dataset['play'].count('Yes'))/n

    h_play=mlog(p_play_no)+mlog(p_play_yes)

    l1entropies=defaultdict(int)
    l1igs=defaultdict(int)
    gain_ratios=defaultdict(int)
    for attr in dataset.keys():
        if attr!='day' and attr!='play':
            print attr
            ucs=Counter(dataset[attr])#.most_common()
            print ucs
            entropies=[]
            wtentropies=[]
            split_infos=[]
            for attrvalue in ucs.keys():
                subsection=[]
                for i in range(int(n)):
                    if dataset[attr][i]==attrvalue:
                        subsection.append(dataset['play'][i])
                #print attrvalue,len(subsection)
                p_play_no=float(subsection.count('No'))/float(len(subsection))
                p_play_yes=float(subsection.count('Yes'))/float(len(subsection))
                #print p_play_no, p_play_yes
                entropy=mlog(p_play_no)+mlog(p_play_yes)
                entropies.append(entropy)
                wtentropies.append(float(ucs[attrvalue])*entropy/float(len(dataset[attr])))
                #print entropies
                split_infos.append(mlog(float(ucs[attrvalue]/float(len(dataset)))))
            attrentropy=sum(wtentropies)
            attr_split_info=sum(split_infos)
            l1entropies[attr]=attrentropy
            l1igs[attr]=h_play-attrentropy
            gain_ratios[attr]=l1igs[attr]/attr_split_info
            

    print h_play
    print l1entropies
    print l1igs
    print gain_ratios

    selected=maximize(gain_ratios)
    print "Selected Attribute: "+selected
    return selected
        
iterationno=1
selected=best_attribute(data)


values=Counter(data[selected])
for value in values.keys():
    if values[value]>1:
        dataset=defaultdict(list)
        for attr in data.keys():
            if attr!=selected:
                for i in range(len(data[attr])):
                    if data[selected][i]==value:
                        dataset[attr].append(data[attr][i])
        print value
        print dataset
        best_attribute(dataset)
        

