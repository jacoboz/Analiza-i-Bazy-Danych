import pandas as pd
import math

file = '../Analysis Data/weather.csv'

data = pd.read_csv(file)
data_new = {}
counter = 0
# data

for row in data.itertuples():
    for day in range(1,31):
        if(row[3] != "PRCP"):
            id_ = row[1]
            day_ = row[2]+'-'+str(day).zfill(2)
            value = row[3+day]
            entry = {row[3]: value}
            if day_ in data_new.keys():
                entry = {**data_new[day_], **entry}
            data_new[day_] = entry



data_new = pd.DataFrame(data_new).T.query('TMAX != "NaN" or TMIN != "NaN"')

file = open('../Analysis Data/weather_tidy.csv', 'w')
file.write('DATE' + data_new.to_csv())
file.close()
