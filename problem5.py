from datetime import datetime
import csv
with open('salesdata.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    lst_all=[]
    for line in csv_reader:
        lst_all.append(line)
    #print(lst_all)


def calculate_ytd_sales(input_date):
    
    input_date = datetime.strptime(input_date, '%m/%d/%Y')
    sum=0
    for dt in lst_all[1:]:
        if datetime.strptime(dt[0], '%m/%d/%Y') <= input_date:
            sum=sum+int(dt[1])
    
    
    

    return sum


input_date =input("Enter date : ")

ytd_value=calculate_ytd_sales(input_date)


print("The ytd value is",ytd_value)

