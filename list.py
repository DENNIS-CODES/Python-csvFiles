import csv
#fields name
fields = ['Date', 'Time', 'Trade_type', 'Eth_price','Token_amount', 'Eth_amount', 'Wallet_address']

#data rows of csv files
rows = [
    ['2021-07-07', '22:19:59', 'sell', '0.0007176', '184,449,624,581', '0.05604492', '0xbbcb2dfgswgfsjdf']
] 

with open('marketinfo_file.csv', 'w') as f:
    #using csv_writer method  csv package
    writer = csv.writer(f)

    writer.writerow(fields)
    writer.writerows(rows)