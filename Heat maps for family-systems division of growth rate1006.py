# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:07:19 2020

@author: caiwei
"""
from pyecharts import Map, Timeline
import xlrd
xlsfile = r"c:\Users\hp\Desktop\countries-aggregated_xls_1006.xls"  # Define data file location
book = xlrd.open_workbook(xlsfile)  # Open data file
sheet_name = book.sheet_by_name(u'Sheet1')  # Get sheet 1 by name

# name for countries or regions
attr = ["Afghanistan", 
"Albania", 
"Algeria", 
"Andorra", 
"Angola", 
"Antigua and Barb.", 
"Argentina", 
"Armenia", 
"Australia", 
"Austria", 
"Azerbaijan", 
"Bahamas", 
"Bahrain", 
"Bangladesh", 
"Barbados", 
"Belarus", 
"Belgium", 
"Belize", 
"Benin", 
"Bhutan", 
"Bolivia", 
"Bosnia and Herz.", 
"Botswana", 
"Brazil", 
"Brunei", 
"Bulgaria", 
"Burkina Faso", 
"Myanmar", 
"Burundi", 
"Cape Verde", 
"Cambodia", 
"Cameroon", 
"Canada", 
"Central African Rep.", 
"Chad", 
"Chile", 
"China", 
"Colombia", 
"Comoros", 
"Dem. Rep. Congo", 
"Congo", 
"Costa Rica", 
"Côte d'Ivoire", 
"Croatia", 
"Cuba", 
"Cyprus", 
"Czech Rep.", 
"Denmark", 
"Djibouti", 
"Dominica", 
"Dominican Rep.", 
"Ecuador", 
"Egypt", 
"El Salvador", 
"Eq. Guinea", 
"Eritrea", 
"Estonia", 
"Swaziland", 
"Ethiopia", 
"Fiji", 
"Finland", 
"France", 
"Gabon", 
"Gambia", 
"Georgia", 
"Germany", 
"Ghana", 
"Greece", 
"Grenada", 
"Guatemala", 
"Guinea", 
"Guinea-Bissau", 
"Guyana", 
"Haiti", 
"Honduras", 
"Hungary", 
"Iceland", 
"India", 
"Indonesia", 
"Iran", 
"Iraq", 
"Ireland", 
"Israel", 
"Italy", 
"Jamaica", 
"Japan", 
"Jordan", 
"Kazakhstan", 
"Kenya", 
"Korea", 
"Kuwait", 
"Kyrgyzstan", 
"Lao PDR", 
"Latvia", 
"Lebanon", 
"Lesotho", 
"Liberia", 
"Libya", 
"Liechtenstein", 
"Lithuania", 
"Luxembourg", 
"Madagascar", 
"Malawi", 
"Malaysia", 
"Mali", 
"Malta", 
"Mauritania", 
"Mauritius", 
"Mexico", 
"Moldova", 
"Mongolia", 
"Montenegro", 
"Morocco", 
"Mozambique", 
"Namibia", 
"Nepal", 
"Netherlands", 
"New Zealand", 
"Nicaragua", 
"Niger", 
"Nigeria", 
"Macedonia", 
"Norway", 
"Oman", 
"Pakistan", 
"Panama", 
"Papua New Guinea", 
"Paraguay", 
"Peru", 
"Philippines", 
"Poland", 
"Portugal", 
"Qatar", 
"Romania", 
"Russia", 
"Rwanda", 
"Saint Kitts and Nevis", 
"Saint Lucia", 
"Saint Vincent and the Grenadines", 
"San Marino", 
"São Tomé and Principe", 
"Saudi Arabia", 
"Senegal", 
"Serbia", 
"Seychelles", 
"Sierra Leone", 
"Singapore", 
"Slovakia", 
"Slovenia", 
"Somalia", 
"South Africa", 
"South Sudan", 
"Spain", 
"Sri Lanka", 
"Sudan", 
"Suriname", 
"Sweden", 
"Switzerland", 
"Syria", 
"Tajikistan", 
"Tanzania", 
"Thailand", 
"Timor-Leste", 
"Togo", 
"Trinidad and Tobago", 
"Tunisia", 
"Turkey", 
"Uganda", 
"Ukraine", 
"United Arab Emirates", 
"United Kingdom", 
"Uruguay", 
"United States", 
"Uzbekistan", 
"Venezuela", 
"Vietnam", 
"Palestine", 
"W. Sahara", 
"Yemen", 
"Zambia", 
"Zimbabwe"]

#date

data = ['2020/1/22', 
'2020/1/23', 
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
'2020/9/2', 
'2020/9/3']

tl = Timeline(is_auto_play=(False), timeline_bottom=0, timeline_play_interval=0.05) # Turn off auto play, the time component is at the bottom, and the playback interval is 0.05 Ms
for j in range(0, 225):
    sj = j*181+1 # Start line
    ej = sj+181 # Termination line
    jvalue = sheet_name.col_values(5, start_rowx=sj, end_rowx=ej)
    d = data[j]
    covidmap = (
             Map("{}Growth rate Family-system".format(d), width=4000, height=2000)
             .add(
             "", 
             attr, 
             jvalue, 
             visual_range=[0,9], 
             maptype="world", 
             is_visualmap=True, 
             visual_top=100, 
             visual_text_color='#000', 
             is_map_symbol_show=False)
    )
    tl.add(covidmap, data[j])

tl.render(path="Family-system division.html")