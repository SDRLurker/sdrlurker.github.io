# -*- coding: utf-8 -*-
import pandas.io.data as web
import datetime
import numpy as np
import matplotlib.pyplot as plt

start = datetime.datetime(2015,1,2)
end = datetime.datetime(2016,7,22)
f1 = web.DataReader("^DJI",'yahoo',start,end)
f2 = web.DataReader("^KS11",'yahoo',start,end)

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

x_data = []
y_data = []
for single_date in daterange(start, end):
        date_str = single_date.strftime('%Y-%m-%d')
        try:
                f1_close = f1.ix[date_str]['Close']
        except:
                continue
        try:
                f2_close = f2.ix[date_str]['Close']
        except:
                continue
        try:
                print(date_str, f1_close, f2_close)
                x_data.append(f1_close)
                y_data.append(f2_close)
        except:
                pass
                
def make_poly_x(pn, x_data):
    x_datas = []
    for n in range(pn+1):
        x_datas.append([ x ** n for x in x_data ])
    return x_datas
        
def print_hypothesis(pn, theta):
    print('h(X) = ')
    for i, element in enumerate(theta):
        if i == len(theta) - 1:
            print(element.item(0), " X ** ", i)
        else:
            print(element.item(0), " X ** ", i, " + ")

def get_hypothesis(pn, theta, x):
    y = 0
    for i, element in enumerate(theta):
        y += ( element.item(0) * ( x ** i) )
    return y
    
def get_sumerror(pn, theta, x_data, y_data):
    s = 0
    for i, x in enumerate(x_data):
      s += ( (y_data[i] - get_hypothesis(pn, theta, x)) ** 2)
    return s
    
print()
POLY = 1
x_datas = make_poly_x(POLY, x_data)
X = np.matrix(x_datas).transpose()
Xt = np.matrix(x_datas)
Y = np.matrix(y_data).transpose()
theta = np.dot(np.dot(np.linalg.pinv(np.dot(Xt, X)), Xt), Y)
print_hypothesis(POLY, theta)
print('get_sumerror : ', get_sumerror(POLY, theta, x_data, y_data))

print()
x_test = 18313.77
y_test = get_hypothesis(POLY, theta, x_test)

print('2016-08-02 DOW30 : ', x_test)
print('2016-08-02 estimated KOSPI : ', y_test)
print('2016-08-02 KOSPI : ', 2019.03)

plt.plot(x_data, y_data, 'ro')

line_x = [ x for x in range( int(min(x_data)), int(max(x_data)) ) ]
line_y = [ get_hypothesis(POLY, theta, x) for x in range( int(min(x_data)), int(max(x_data)) ) ]
plt.plot(line_x, line_y)
plt.show()
