#here i thout to make a new list
#and make for loop to the old list and put conditions
#note here i use python 2.6
def fransform(list):
    list2=[]
    for i in list:
        if(i==1):
            list2.append("one");
        elif(i==2):
            list2.append("tow");
        elif(i==3):
            list2.append("three");
        elif(i==4):
            list2.append("four");
        elif(i==5):
            list2.append("five");
        elif (i == 6):
            list2.append("six");
        elif (i == 7):
            list2.append("seven");
        elif (i == 8):
            list2.append("eight");
        elif (i == 9):
            list2.append("nine");
        elif (i == 0):
            list2.append("zero");

    return list2



list=[1,2,3,6,8];
new_list=fransform(list);
print new_list;