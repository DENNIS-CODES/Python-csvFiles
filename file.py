#.CSV(Comma Seperated Values file)
#is atype of plain text file that uses specific structuring to arrange tabular data
#because its a plain text file, it can contain only actual text data(printable ASCII or Unicode) characters.
#.CSV file uses a comma to separate each specifc data value
#CSV files are created by programs that handle large amounts of data 
#there are convinient way to export data from spreadsheets and databases as well as import or use it in other programs
#eg u can export the results of a data mining program to a CSV file and then import that into a spreadsheet to analyze the data 
#generate graphs for a presentation, or prepare a report for publication

import csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#If quoting is set to csv.QUOTE_MINIMAL, then .writerow() will quote fields only if they contain the delimiter or the quotechar. This is the default case.
#If quoting is set to csv.QUOTE_ALL, then .writerow() will quote all fields.
#If quoting is set to csv.QUOTE_NONNUMERIC, then .writerow() will quote all field containing text data and convert all numeric fields to the float data type
#If quoting is set to csv.QUOTE_NONE, then .writerow() will escape delimiters instead of quoting them. In this case, you also must provide a value for the escapechar optional parameter.

    employee_writer.writerow(['Dennis Mwangi', 'Developer','November'])
    employee_writer.writerow(['Vinicent Opiyo', 'Agile', 'February'])