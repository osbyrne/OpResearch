from random import *
import copy

def randTable(size):
    datalist=[]
    order=[]
    sizeorder=0
    provision=[]
    for i in range(size):
        temp=[]
        ordertemp=randint(1,100)
        sizeorder+=ordertemp
        order.append(ordertemp)
        for j in range(size):
            temp.append(randint(1,100))
        datalist.append(temp)
    """for idx in range(size-1):
        provision.append(randint(1,sizeorder-sum(provision)-size+idx))
    provision.append(sizeorder-sum(provision))
    shuffle(provision)
    """
    provision=copy.deepcopy(order)
    shuffle(provision)
    return(datalist,order,provision)