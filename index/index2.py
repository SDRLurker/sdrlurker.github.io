# -*- coding: utf-8 -*-
import pandas.io.data as web
import datetime
import numpy as np
start = datetime.datetime(2015,1,2)
end = datetime.datetime(2016,7,25)
f1 = web.DataReader("^DJI",'yahoo',start,end)
f2 = web.DataReader("^N225",'yahoo',start,end)
f3 = web.DataReader("^KS11",'yahoo',start,end)

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

x1_data = []
x2_data = []
y_data = []
print("date_str", "DJI_close", "N225_close", "KOSPI_close")
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
                f3_close = f3.ix[date_str]['Close']
        except:
                continue

        try:
                print(date_str, f1_close, f2_close, f3_close)
                x1_data.append(f1_close)
                x2_data.append(f2_close)
                y_data.append(f3_close)
        except:
                pass

ones = [ 1 for y in y_data ]
x_datas = [ones, x1_data, x2_data]
X = np.matrix(x_datas).transpose()
print(X)
Xt = np.matrix(x_datas)
Y = np.matrix(y_data).transpose()
theta = np.dot(np.dot(np.linalg.pinv(np.dot(Xt, X)), Xt), Y)
print('h(X) = ', theta[1], 'x1(DOW) + ', theta[2], 'x2(N225) + ', theta[0])

x1_test = 18313.77
x2_test = 16391.45
y_test = theta[2] * x2_test + theta[1] * x1_test + theta[0]
print('2016-08-02 DOW30 : ', x1_test)
print('2016-08-02 N225  : ', x2_test)
print('2016-08-02 estimated KOSPI : ', y_test)
print('2016-08-02 KOSPI : ', 2019.03)

x1_test = 18570.849609
x2_test = 16627.25
y_test = theta[2] * x2_test + theta[1] * x1_test + theta[0]
print('2016-07-22 DOW30 : ', x1_test)
print('2016-07-22 N225  : ', x2_test)
print('2016-07-22 estimated KOSPI : ', y_test)
print('2016-07-22 KOSPI : ', 2010.339966)
