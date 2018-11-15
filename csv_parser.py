import csv
from datetime import datetime

file_to_parse = 'rejestracjeOCP.csv'
report_file = 'report.csv'

with open(file_to_parse) as f:
    print('start')
    reader = csv.DictReader(f)

    seg = 0
    map = 0
    #map_ptp = 0
    ptp = 0

    dictionary = {}

    for row in reader:
        date = row['REGISTRATION_DATE'][:8]

        is_exists = dictionary.keys().__contains__(date)

        if not is_exists:
            seg = 0
            map = 0
            ptp = 0
            dictionary[date] = {'seg': seg, 'map': map, 'ptp': ptp}

        if row['SEGMENT'] == 'PROSPECT':
            seg += 1
        elif row['ACCOUNT_TYPE_MAP'] == 'CUSTOMER_MAP':
            map +=1
        elif row['ACCOUNT_TYPE_PTP'] == 'PTP_CUSTOMER':
            ptp += 1

        if dictionary.keys().__contains__(date):
            dictionary[date] = {'seg': seg, 'map': map, 'ptp': ptp}

    with open(report_file, 'w') as f:
        columnTitleRow = "REGISTRATION_DATE|PROSPECT|CUSTOMER_MAP|PTP_CUSTOMER\n"
        f.write(columnTitleRow)

        for key in dictionary.keys():
            column1 = key
            column2 = dictionary[key]['seg']
            column3 = dictionary[key]['map']
            column4 = dictionary[key]['ptp']
            row = '{}|{}|{}|{}\n'.format(column1, column2, column3, column4)
            f.write(row)




