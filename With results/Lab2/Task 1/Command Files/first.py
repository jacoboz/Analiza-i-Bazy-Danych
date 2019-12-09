import re

file = open('../Analysis Data/weather.txt')
data = file.read()
file.close()

data = re.sub('[BDS]?[\t ]+(OI|OS|SI|I+|S+)[\t ]*',',',data)
data = re.sub('[\t ]+',',',data)
data = re.sub('\s*,[\t ]*\n','\n',data)
data = re.sub('MX000017004(\d\d\d\d)(\d\d)(\w\w\w\w)','MX000017004,\g<1>-\g<2>,\g<3>',data)
data = data.replace('-9999','')

#Create headers
header = 'id,year-month,var'
# header = 'year-month,var'
for i in range(1,33):
    header += ',Day'+str(i)
    
#Connect headers with data
data = header+'\n'+data

#Save *.txt file as *.csv 
file = open('../Analysis Data/weather.csv','w')
file.write(data)
file.close()
