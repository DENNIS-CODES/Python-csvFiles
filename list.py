import csv
#fields name
fields = ['Date', 'Time', 'Trade_type', 'Eth_price','Token_amount', 'Eth_amount', 'Wallet_address']

#data rows of csv files
rows = [
    ['2021-07-07', '22:19:59', 'sell', '0.0007176', '184,449,624,581', '0.05604492', '0xbbcb2dfgswgfsjdf'],
    ['2021-07-07', '22:20:00', 'buy', '0.0008476', '184,449,624,581', '0.05604492', '0xbbcb2dfgswgfsjdf'],
    ['2021-07-07', '22:21:01', 'sell', '0.0007124', '184,449,624,581', '0.05604492', '0xbbcb2dfgswgfsjdf'],
    ['2021-07-07', '22:22:02', 'sell', '0.0007826', '184,449,624,581', '0.05604492', '0xbbcb2dfgswgfsjdf'],
    ['2021-07-07', '22:23:03', 'buy', '0.0007036', '184,449,624,581', '0.05604492', '0xbbcb2dfgswgfsjdf'],
    ['2021-07-07', '22:24:04', 'sell', '0.0000876', '184,449,624,581', '0.05604492', '0xbbcb2dfgswgfsjdf'],
    ['2021-07-07', '22:25:05', 'buy', '0.0007526', '184,449,624,581', '0.05604492', '0xbbcb2dfgswgfsjdf'],
    ['2021-07-07', '22:26:06', 'buy', '0.00074566', '184,449,624,581', '0.05604492', '0xbbcb2dfgswgfsjdf'],
    ['2021-07-07', '22:27:07', 'sell', '0.0007204', '184,449,624,581', '0.05604492', '0xbbcb2dfgswgfsjdf'],
    ['2021-07-07', '22:28:08', 'buy', '0.0007143', '184,449,624,581', '0.05604492', '0xbbcb2dfgswgfsjdf'],
    ['2021-07-07', '22:29:09', 'sell', '0.0000923', '184,449,624,581', '0.05604492', '0xbbcb2dfgswgfsjdf'],
    ['2021-07-07', '22:30:10', 'buy', '0.0003947', '184,449,624,581', '0.05604492', '0xbbcb2dfgswgfsjdf'],
    ['2021-07-07', '22:31:11', 'sell', '0.00028045', '184,449,624,581', '0.05604492', '0xbbcb2dfgswgfsjdf']
] 

with open('marketinfo_file.csv', 'w') as f:
    #using csv_writer method  csv package
    writer = csv.writer(f)

    writer.writerow(fields)
    writer.writerows(rows)