#PyBank Analysis to create output to terminal and to text file

import os                                                               #import os module to allow to create file paths accross operating systems
import csv                                                              #import csv module for reading csv files

#csvpath = "Resources/budget_data.csv"
csvpath=os.path.join('Resources','budget_data.csv')       
               #source file and location in network folder

output_p = os.path.join('Anlysis','financial_analysis.txt')      

with open(csvpath) as csvfile :
    csvreader=csv.reader(csvfile,delimiter=',')                        
    csv_header=next(csvreader)                                          

    row_count=1                                                       
    change_list=[]                                            
    max_increase=0                                                   
    max_increase_month=""                                           
    max_decrease=0                                                     
    max_decrease_month=""                                       
    first_Row=next(csvreader)                                          
    prev_net=int(first_Row[1])                                          #setting cell B2 as the previous value to calc change in profit
    total_sum=prev_net                                                  
    
    for row in csvreader:
        row_count = row_count + 1                                   
        
        if row_count>0:                                         
            total_sum = total_sum + int(row[1])                       
        total_sum_format="${}".format(total_sum)
    
        change = int(row[1]) - prev_net                                 #calculate the change from the previous value
        change_list.append(change)                                      #append each change calc for each row of data to change_list
        prev_net = int(row[1])                                          #update the previous value for the next iteration

        if change > max_increase:                                       #check if the change is the greatest increase
            max_increase = change
            max_increase_format="${}".format(max_increase)
            max_increase_month=row[0]
        prev_net=int(row[1])

        if change < max_decrease:                                       #check if the change is the greatest decrease
            max_decrease = change
            max_decrease_format="${}".format(max_decrease)
            max_decrease_month=row[0]
        prev_net=int(row[1])

    average_change = sum(change_list) / (row_count-1)                   #calculate the average change
    average_change_format="${:.2f}".format(average_change)

    #Print output to terminal
    print()
    print("Financial Analysis")
    print()
    print("----------------------------------")
    print()
    print(f"Total Months: {row_count}")                                 #print total months listed in csv file based on row_count
    print()
    print(f"Total: {total_sum_format}")                                 #print sum of column B total profit/loss 
    print()
    print(f"Average Change:{average_change_format} ")                   #print average change in profit/loss
    print()
    print(f"Greatest Increase in Profits: {max_increase_month} ({max_increase_format}) ")       #print month with biggest increase in profit/loss
    print()
    print(f"Greatest Decrease in Profits: {max_decrease_month} ({max_decrease_format}) ")       #print month with biggest decrease in profit/loss


with open(output_p,"w") as output :       
    #Print output to "financial analysis.txt" file
    output.write("Financial Analysis\n")
    output.write("\n")
    output.write("----------------------------------\n")
    output.write("\n")
    output.write(f"Total Months: {row_count}\n")
    output.write("\n")
    output.write(f"Total: {total_sum_format}\n")
    output.write("\n")
    output.write(f"Average Change: {average_change_format}\n")
    output.write("\n")
    output.write(f"Greatest Increase in Profits: {max_increase_month} ({max_increase_format})\n")
    output.write("\n")
    output.write(f"Greatest Decrease in Profits: {max_decrease_month} ({max_decrease_format})\n")