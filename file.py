#.CSV(Comma Seperated Values file)
#is atype of palin text file that uses specific structuring to arrange tabular data
#because its a plain text file, it can contain only actual text data(printable ASCII or Unicode) characters.
#.CSV file uses a comma to separate each specifc data value
#CSV files are created by programs that handle large amounts of data 
#there are convinient way to export data from spreadsheets and databases as well as import or use it in other programs
#eg u can export the results of a data mining program to a CSV file and then import that into a spreadsheet to analyze the data 
#generate graphs for a presentation, or prepare a report for publication

import csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['Dennis Mwangi', 'Developer','November'])
    employee_writer.writerow(['Vinicent Opiyo', 'Agile', 'February'])