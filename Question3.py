#note here i use python 2.6

import csv
with open('oscar.csv','r') as oscar:
    roscar=csv.reader(oscar)
    actor=[]
    year=[]
    move=[]
    count=[]
    actor_row=[]
#here i divide the csv to many list
    for i in roscar:
        actor.append(i[3])
        year.append(i[2])
        move.append(i[4])

#here the actor who is repeted mor than any other he will be
#the actor who has more Oscars from the others


    for j in actor:
        x=actor.count(j)
        count.append(x)
mx_nomber_oscar_who_had= max (count)
ind_the_mx=count.index(mx_nomber_oscar_who_had)
print "the actor who has more Oscars from the others "
print actor[ind_the_mx]
#here the actor who has the biger age he will be
#the actor who is the oldest actor or actress who got the Oscar, in what year and for what movie


the_oldest=max(year)
ind_old=year.index(the_oldest)
print "the actor who is the oldest actor or actress who got the Oscar"
print actor[ind_old]
print ' for what movie'
print move[ind_old]
print ", in what year "
print year[ind_old]

#here the actor who is repeted Respectively he will be
#name of the actor who got the more than Oscar in row

lenth=len(actor)-1

for k in actor:
    z=actor.index(k)
    if(z<lenth):
        z=z+1
    else:
        break
    if(k == actor[z]):
        if(k not in actor_row):
            actor_row.append(k)

print 'name of the actor who got the more than Oscar in row'
for d in actor_row:
   print d


