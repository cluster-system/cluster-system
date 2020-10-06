# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 22:32:02 2020

@author: caiwei
"""
import numpy as np
import xlrd
from pyecharts import HeatMap


xlsfile = r"c:\Users\hp\Desktop\countries-aggregated_xls_1006.xls"  # Define data file location
book = xlrd.open_workbook(xlsfile)  # Open data file
sheet_name = book.sheet_by_name(u'Sheet1')

# Calculate the number of transfers between families per day
for d in range(224):
    sd = d*181+1
    ed = sd+181
    ed2 = ed+181
    a = np.asarray(sheet_name.col_values(5, start_rowx=sd, end_rowx=ed))
    b = np.asarray(sheet_name.col_values(5, start_rowx=ed, end_rowx=ed2))
    for l in range(10):
        for h in range(10):
            exec('pos{}{}{}=np.intersect1d(np.where(a == l),np.where(b == h)).size'.format(d,l,h))

# Get the daily transfer matrix
for day in range(224):
    exec('t{}=[]'.format(day))
    for lie in range(10):
        exec('t{}.append([])'.format(day))
        for han in range(10):
            exec('di = pos{}{}0+pos{}{}1+pos{}{}2+pos{}{}3+pos{}{}4+pos{}{}5+\
                 pos{}{}6+pos{}{}7+pos{}{}8+pos{}{}9'
                 .format(day,lie,day,lie,day,lie,day,lie,day,lie,day,lie,\
                         day,lie,day,lie,day,lie,day,lie,))
            if di == 0:
                # If a family is 0 the day before yesterday, then this row of the transfer matrix is 0
                exec('t{}[lie].append(0)'.format(day)) 
            else:
                exec('t{}[lie].append(pos{}{}{}/di)'.format(day, day, lie, han))

# Count the number of each family per day
for da in range(224):
    sda = da*181+1
    eda = sda+181
    ada = np.asarray(sheet_name.col_values(5, start_rowx=sda, end_rowx=eda))
    for ff in range(10):
        exec('f_num{}{}=sum(ada=={})'.format(da,ff,ff))

# Prediction of the next day's family numbers by transfer matrix
for da1 in range(223):
    # sda1 = da1*181+1
    # eda1 = sda1+181
    # ada1 = np.asarray(sheet_name.col_values(5, start_rowx=sda1, end_rowx=eda1))
    for fff in range(10):
        exec('fy_num{}{}=\
             f_num{}0*t{}[0][{}]+\
             f_num{}1*t{}[1][{}]+\
             f_num{}2*t{}[2][{}]+\
             f_num{}3*t{}[3][{}]+\
             f_num{}4*t{}[4][{}]+\
             f_num{}5*t{}[5][{}]+\
             f_num{}6*t{}[6][{}]+\
             f_num{}7*t{}[7][{}]+\
             f_num{}8*t{}[8][{}]+\
             f_num{}9*t{}[9][{}]'
             .format(da1+2, fff, \
                     da1+1, da1, fff, \
                     da1+1, da1, fff, \
                     da1+1, da1, fff, \
                     da1+1, da1, fff, \
                     da1+1, da1, fff, \
                     da1+1, da1, fff, \
                     da1+1, da1, fff, \
                     da1+1, da1, fff, \
                     da1+1, da1, fff, \
                     da1+1, da1, fff))
            
# Find the relative error
tc = [] 
for dac in range(222):
    tc.append([])
    for fc in range(10):
        exec('zhong = f_num{}{}'.format(dac+2, fc))
        exec('zz = fy_num{}{}'.format(dac+2,fc))
        if zhong == 0:
            # If the actual value is 0, the value is 1
            exec('tc[dac].append(abs(fy_num{}{}-f_num{}{})/(f_num{}{}+1)*100)'
                 .format(dac+2, fc, dac+2, fc, dac+2, fc))
        else:
            exec('tc[dac].append(abs(fy_num{}{}-f_num{}{})/(f_num{}{})*100)'
                 .format(dac+2, fc, dac+2, fc, dac+2, fc))

# Find absolute error
tcj = []            
for dacj in range(222):
    tcj.append([])
    for fcj in range(10):
        exec('tcj[dacj].append(abs(fy_num{}{}-f_num{}{}))'
                 .format(dacj+2, fcj, dacj+2, fcj))

# Find the fiducial error, denominator 181 (upper prediction limit)
tcy = []            
for dacy in range(222):
    tcy.append([])
    for fcy in range(10):
        exec('tcy[dacy].append(abs(fy_num{}{}-f_num{}{})/181*100)'
                 .format(dacy+2, fcy, dacy+2, fcy))

x_axis = [
'2020/1/24', 
'2020/1/25', 
'2020/1/26', 
'2020/1/27', 
'2020/1/28', 
'2020/1/29', 
'2020/1/30', 
'2020/1/31', 
'2020/2/1', 
'2020/2/2', 
'2020/2/3', 
'2020/2/4', 
'2020/2/5', 
'2020/2/6', 
'2020/2/7', 
'2020/2/8', 
'2020/2/9', 
'2020/2/10', 
'2020/2/11', 
'2020/2/12', 
'2020/2/13', 
'2020/2/14', 
'2020/2/15', 
'2020/2/16', 
'2020/2/17', 
'2020/2/18', 
'2020/2/19', 
'2020/2/20', 
'2020/2/21', 
'2020/2/22', 
'2020/2/23', 
'2020/2/24', 
'2020/2/25', 
'2020/2/26', 
'2020/2/27', 
'2020/2/28', 
'2020/2/29', 
'2020/3/1', 
'2020/3/2', 
'2020/3/3', 
'2020/3/4', 
'2020/3/5', 
'2020/3/6', 
'2020/3/7', 
'2020/3/8', 
'2020/3/9', 
'2020/3/10', 
'2020/3/11', 
'2020/3/12', 
'2020/3/13', 
'2020/3/14', 
'2020/3/15', 
'2020/3/16', 
'2020/3/17', 
'2020/3/18', 
'2020/3/19', 
'2020/3/20', 
'2020/3/21', 
'2020/3/22', 
'2020/3/23', 
'2020/3/24', 
'2020/3/25', 
'2020/3/26', 
'2020/3/27', 
'2020/3/28', 
'2020/3/29', 
'2020/3/30', 
'2020/3/31', 
'2020/4/1', 
'2020/4/2', 
'2020/4/3', 
'2020/4/4', 
'2020/4/5', 
'2020/4/6', 
'2020/4/7', 
'2020/4/8', 
'2020/4/9', 
'2020/4/10', 
'2020/4/11', 
'2020/4/12', 
'2020/4/13', 
'2020/4/14', 
'2020/4/15', 
'2020/4/16', 
'2020/4/17', 
'2020/4/18', 
'2020/4/19', 
'2020/4/20', 
'2020/4/21', 
'2020/4/22', 
'2020/4/23', 
'2020/4/24', 
'2020/4/25', 
'2020/4/26', 
'2020/4/27', 
'2020/4/28', 
'2020/4/29', 
'2020/4/30', 
'2020/5/1', 
'2020/5/2', 
'2020/5/3', 
'2020/5/4', 
'2020/5/5', 
'2020/5/6', 
'2020/5/7', 
'2020/5/8', 
'2020/5/9', 
'2020/5/10', 
'2020/5/11', 
'2020/5/12', 
'2020/5/13', 
'2020/5/14', 
'2020/5/15', 
'2020/5/16', 
'2020/5/17', 
'2020/5/18', 
'2020/5/19', 
'2020/5/20', 
'2020/5/21', 
'2020/5/22', 
'2020/5/23', 
'2020/5/24', 
'2020/5/25', 
'2020/5/26', 
'2020/5/27', 
'2020/5/28', 
'2020/5/29', 
'2020/5/30', 
'2020/5/31', 
'2020/6/1', 
'2020/6/2', 
'2020/6/3', 
'2020/6/4', 
'2020/6/5', 
'2020/6/6', 
'2020/6/7', 
'2020/6/8', 
'2020/6/9', 
'2020/6/10', 
'2020/6/11', 
'2020/6/12', 
'2020/6/13', 
'2020/6/14', 
'2020/6/15', 
'2020/6/16', 
'2020/6/17', 
'2020/6/18', 
'2020/6/19', 
'2020/6/20', 
'2020/6/21', 
'2020/6/22', 
'2020/6/23', 
'2020/6/24', 
'2020/6/25', 
'2020/6/26', 
'2020/6/27', 
'2020/6/28', 
'2020/6/29', 
'2020/6/30', 
'2020/7/1', 
'2020/7/2', 
'2020/7/3', 
'2020/7/4', 
'2020/7/5', 
'2020/7/6', 
'2020/7/7', 
'2020/7/8', 
'2020/7/9', 
'2020/7/10', 
'2020/7/11', 
'2020/7/12', 
'2020/7/13', 
'2020/7/14', 
'2020/7/15', 
'2020/7/16', 
'2020/7/17', 
'2020/7/18', 
'2020/7/19', 
'2020/7/20', 
'2020/7/21', 
'2020/7/22', 
'2020/7/23', 
'2020/7/24', 
'2020/7/25', 
'2020/7/26', 
'2020/7/27', 
'2020/7/28', 
'2020/7/29', 
'2020/7/30', 
'2020/7/31', 
'2020/8/1', 
'2020/8/2', 
'2020/8/3', 
'2020/8/4', 
'2020/8/5', 
'2020/8/6', 
'2020/8/7', 
'2020/8/8', 
'2020/8/9', 
'2020/8/10', 
'2020/8/11', 
'2020/8/12', 
'2020/8/13', 
'2020/8/14', 
'2020/8/15', 
'2020/8/16', 
'2020/8/17', 
'2020/8/18', 
'2020/8/19', 
'2020/8/20', 
'2020/8/21', 
'2020/8/22', 
'2020/8/23', 
'2020/8/24', 
'2020/8/25', 
'2020/8/26', 
'2020/8/27', 
'2020/8/28', 
'2020/8/29', 
'2020/8/30', 
'2020/8/31', 
'2020/9/1', 
'2020/9/2']

y_axis = ['f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9']

# Drawing absolute error thermal diagram
data = [[i, j, tcj[i][j]] for i in range(222) for j in range(10)]
heatmap = HeatMap()
heatmap.add(
    "",
    x_axis,
    y_axis,
    data,
    is_visualmap=True,
    visual_text_color="#000",
    visual_range=[0, 55], 
    visual_orient="horizontal",
)
heatmap.render(path="Absolute error_heatmap_1006.html")

# Draw the relative error thermal diagram, where the true value is 0, the value is 1
data = [[i, j, tc[i][j]] for i in range(222) for j in range(10)]
heatmap = HeatMap()
heatmap.add(
    "",
    x_axis,
    y_axis,
    data,
    is_visualmap=True,
    visual_text_color="#000",
    visual_orient="horizontal",
)
heatmap.render(path="Relative error_heatmap_1006.html")

# Drawing thermal diagram of fiducial error
data = [[i, j, tcy[i][j]] for i in range(222) for j in range(10)]
heatmap = HeatMap()
heatmap.add(
    "",
    x_axis,
    y_axis,
    data,
    is_visualmap=True,
    visual_range=[0, 30], 
    visual_text_color="#000",
    visual_orient="horizontal",
)
heatmap.render(path="Fiducial error_heatmap_1006.html")
