#input data file=data.csv
#output data file=new_data.csv
import csv
def comparedates(old_date,curr_date):
    j=0
    k=0
    while(j<3):
        if old_date[j]==curr_date[k]:
            k=k+1
            j=j+1
        elif old_date[j]>curr_date[k]:
            return 0
        else:
            return 1
with open('data.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    lst_all=[]
    for line in csv_reader:
        lst_all.append(line)
    dict={}
    for i in lst_all:
        tup=(i[0],i[1])
        #if the combination of (product_group_id,product_id) is unique
        if tup not in dict:
            dict[tup]=[i[2],i[3]]
        #if the combination is duplicate so there is a need to compare dates the comparision of the dates is done comparedates function
        else:
            old_date=dict[tup][1].split('-')
            old_date_int = [int(x) for x in old_date]
            curr_date=i[3].split('-')
            curr_date_int = [int(x) for x in curr_date]
            final_date=comparedates(old_date_int,curr_date_int)
            if final_date==1:
                dict[tup]=[i[2],i[3]]
    print(dict)
final_lst=[]
with open('new_data.csv','w') as new_file:
    csv_writer=csv.writer(new_file)
    for val in dict:
        a,b=val
        c,d=dict[val]
        
        csv_writer.writerow([a,b,c,d])


    
        
