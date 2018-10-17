#in this question i make another list and puted the elemant of list1 in even position
#and put the elemant of list2 in odd position.
#note here i use python 2.6
def comcat(list1,list2):
    list3=[]
    x=0
    y=1
    for i in list1:
        list3.insert(x,i)
        x=x+2
    for j in list2:
        list3.insert(y, j)
        y = y + 2
    return list3





list1=[1,'a',2,'b',3]
list2=[4,'c',5,'d',6]
new_list=comcat(list1,list2);
print new_list