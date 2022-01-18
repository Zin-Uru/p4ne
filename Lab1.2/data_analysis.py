#!/usr/bin/python3

from matplotlib import pyplot as plot
from openpyxl import load_workbook as xls

wb = xls('data_analysis_lab.xlsx')
sheet = wb['Data']


def gv(x):
    return x.value


y = list(map(gv, sheet['A'][1:]))
t = list(map(gv, sheet['C'][1:]))
a = list(map(gv, sheet['D'][1:]))

plot.plot(y, t, label='Температура')
plot.plot(y, a, label='Активность Солнца')
plot.title("Показатели", loc='left')
plot.xlabel("Годы")
plot.ylabel("Температура/Активность")
plot.legend()

plot.show()
