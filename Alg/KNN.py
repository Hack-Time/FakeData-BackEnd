from tkinter import *
from tkinter import ttk
from numpy import *
import numpy as np
import itertools
from codecs import decode
from math import pow

#53 items, 10 events

class date:
    def __init__(self, year, month, date):
        self.y = year
        self.m = month
        self.d = date
    
    def read(str1):
        ld = str1.split('-')
        return date(int(ld[0]), int(ld[1]), int(ld[2]))
    
    def express(self):
        return str(self.y) + '-' + str(self.m) + '-' + str(self.d)
    
    def prev(self):
        self.d -= 1
        if self.d == 0:
            self.m -= 1
            if self.m in [0,1,3,5,7,8,10]:
                self.d = 31
            elif self.m == 2:
                self.d = 28 + RunYear(self.y)
            else:
                self.d = 30
        if self.m ==0:
            self.y -= 1
            self.m = 12
    
    def post(self):
        self.d += 1
        if self.d > 31:
            self.d = 1
            self.m += 1
            if self.m > 12:
                self.m = 1
                self.y += 1
        elif self.d > 30:
            if self.m in [4, 6, 9, 11]:
                self.d = 1
                self.m += 1
        elif self.d > 28 + RunYear(self.y):
            if self.m == 2:
                self.m = 3
                self.d = 1
    
    def dist(self, day2):
        m = self
        n = self
        cnt = 0
        print(m.express())
        while (m.express() != day2):
            m.prev()
            cnt += 1
        return cnt
'''
eventLists = [[date(2016, 8, 10).express, date(2017,8,10).express, date(2018, 8, 10).express], 
                [date(2016, 10, 18).express, date(2017, 10, 18).express, date(2018, 10, 18).express],
                [date(2016, 1, 1).express, date(2016, 4, 5).express, date(2016, 5, 1).express, date(2016, 9, 24).express, date(2016, 10, 1).express, date(2017, 1, 1).express, date(2017, 4, 5).express, date(2017, 5, 1).express, date(2017, 9, 24).express, date(2017, 10, 1).express, date(2018, 1, 1).express, date(2018, 4, 5).express, date(2018, 5, 1).express, date(2018, 9, 24).express, date(2018, 10, 1).express],
                [date(2016,1,17).express, date(2017,1,13).express, date(2018,1,23).express],
                [date(2016,7,5).express, date(2017,7,5).express, date(2018,7,5).express],
                [date(2016,6,9).express, date(2017,6,9).express, date(2018,6,9).express],
                [date(2016,5,7).express, date(2016,10,29).express, date(2017,5,13).express, date(2017,10,28).express, date(2018,5,12).express, date(2018,10,27).express],
                [date(2016,5,20).express, date(2017,5,20).express, date(2018,5,20).express],
                [date(2016,12,10).express, date(2017,12,10).express, date(2018,12,10).express],
                [date(2016,9,1).express, date(2017,9,1).express, date(2018,9,1).express],
                [date(2016,2,22).express, date(2017,2,16).express, date(2018,2,25).express],
                [date(2016,6,14).express, date(2016,11,7).express, date(2017,6,14).express, date(2017,11,7).express, date(2018,6,14).express, date(2018,11,7).express],
                [date(2016,6,18).express, date(2016,11,11).express, date(2017,6,18).express, date(2017,11,11).express, date(2018,6,18).express, date(2018,11,11).express]]
'''
eventLists = [['2016-8-10', '2017-8-10', '2018-8-10'],['2016-10-18', '2017-10-18', '2018-10-18'],
                ['2016-1-1', '2016-4-5', '2016-5-1', '2016-9-24', '2016-10-1', '2017-1-1', '2017-4-5', '2017-5-1', '2017-9-24', '2017-10-1', '2018-1-1', '2018-4-5', '2018-5-1', '2018-9-24', '2018-10-1'],
                ['2016-1-17', '2017-1-13', '2018-1-23'], ['2016-7-5', '2017-7-5', '2018-7-5'], ['2016-6-9', '2017-6-9', '2018-6-9'],
                ['2016-5-7, 2016-10-29', '2017-5-13', '2017-10-28', '2018-5-12', '2018-10-27'],
                ['2016-5-20', '2017-5-20', '2018-5-20'],
                ['2016-12-10', '2017-12-10', '2018-12-10'],
                ['2016-9-1', '2017-9-1', '2018-9-1'],['2016-2-22', '2017-2-16', '2018-2-25'],
                ['2016-6-14', '2016-11-7', '2017-6-14', '2017-11-7', '2018-6-14', '2018-11-7'],['2016-6-18', '2016-11-11', '2017-6-18', '2017-11-11', '2018-6-18', '2018-11-11']]

def processDayChara(day0, day1, day2, day3):
    u1 = []
    u2 = []
    u3 = []
    for d0, d1, d2, d3 in zip(day0, day1, day2, day3):
        u1.append(classify(float(d1)/float(d0) - 1))
        u2.append(classify(float(d2)/float(d0) - 1))
        u3.append(classify(float(d3)/float(d0) - 1))
    return [u1, u2, u3]

def classify(data):
    return data

def RunYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

def processInit(allData):
    chara = []
    cntn = 0
    day_1 = []
    day_2 = []
    day_3 = []
    flag = [False for i in range(13)]
    raiseup = [[0 for j in range(50)] for i in range(13)]
    cnt = [0 for i in range(13)]
    day = date(2015, 12, 24)
    for data in allData:
        tmp1 = []
        tmp2 = []
        tmp3 = []
        tmp = []
        today = data
        day.post()
        #print(day.express())
        if cntn <= 3:
            #chara.append([[0 for i in range(50)],[0 for i in range(50)],[0 for i in range(50)],[False for i in range(13)]])
            cntn+=1
            day_3 = day_2
            day_2 = day_1
            day_1 = today
            continue
        for d0,d1,d2,d3 in zip(today, day_1, day_2, day_3):
            if d0 == '' or d1 == '':
                print(d0, d1, d2, d3)
            tmp1.append(classify((float(d2) - float(d3)) / float(d3)))
            tmp2.append(classify((float(d1) - float(d3)) / float(d3)))
            tmp3.append(classify((float(d0) - float(d3)) / float(d3)))
            tmp.append(classify((float(d0) - float(d1)) / float(d1)))
        chara.append([tmp1, tmp2, tmp3, day.express()])
        for i in range(13):
            if flag[i] == True:
                raiseup[i] = add(raiseup[i], tmp)
                cnt[i] += 1
                flag[i] = False
        for eventList in eventLists:
            if day.express() in eventList:
                flag[eventLists.index(eventList)] = True
        day_3 = day_2
        day_2 = day_1
        day_1 = today
    return chara, raiseup, cnt

def similar(l1, l2):
    dist = 0
    for x,y in zip(l1, l2):
        dist += pow(x-y, 2)
    return dist
    #print (dist)

def processKNN(instance, mode, eventList):
    tmp = {}
    cnt = 0
    for i in instance:
        tmp[i[3]] = similar(i[0], mode[0]) + similar(i[1], mode[1]) + similar(i[2], mode[2])
    for i in range(80):
        key = min(tmp, key = tmp.get)
        tmp.pop(key)
        if key in eventList:
            cnt += 1
    if cnt > 1:
        return True
    return False

def add(l1, l2):
    rlt = []
    for x,y in zip(l1, l2):
        rlt.append(x + y)
    return rlt

def sub(l1, l2):
    rlt = []
    for x,y in zip(l1, l2):
        rlt.append(x - y)
    return rlt

def mult(l1, l2):
    rlt = []
    for x,y in zip(l1, l2):
        rlt.append(float(x)*float(y))
    return rlt

def div(l1, l2):
    rlt = []
    for x,y in zip(l1, l2):
        rlt.append(x/y)
    return rlt

def roundl(l1):
    rlt = []
    for i in l1:
        rlt.append(round(i))
    return rlt

def exe(daystr):
    f = open('/Users/kingcos/Documents/GitHub/FakeData-BackEnd/Alg/SimuRes.csv', 'rb')
    data = []
    #print(f.read())
    day = date.read(daystr)
    dist = day.dist('2015-12-24')

    allData = decode(f.read(), encoding = 'ascii').split('\n')
    # print(len(allData))

    for i in allData[:dist]:
        data.append(i[:-1].split(','))
    chara, r, cnt = processInit(data)
    # print(cnt)
    rr = []
    for i in r:
        rr.append(div(i, [cnt[r.index(i)] for j in range(50)]))
        #print(len(i), len(cnt))
    test = []
    #print(len(f.readlines(), dist)
    for i in allData[dist - 4: dist + 1]:
        #print(i)
        test.append(i[:-1].split(','))
        #print(i.split(','))
    #print(test[0])
    # print(len(test))
    mode = processDayChara(test[0], test[1], test[2], test[3])
    event = [processKNN(chara, mode, eventList) for eventList in eventLists]
    # print (event)
    rest = [random.randint(4,20) for i in range(50)]
    # print('stock:', rest)
    rlt = mult(test[3], [1.02 for i in range(50)])
    for i in range(13):
        if event[i]:
            rlt = add(rlt, mult(test[3], rr[i]))
    # print (event)
    return rest, roundl(rlt), allData[dist][:-1].split(',')
    
def main():
    stock, predict, real = exe(input())
    # print(predict)
    # print(real)
    #for x,y in zip(predict, real):
    #    print(int(x) - int(y))

if __name__ == '__main__':
    main()
