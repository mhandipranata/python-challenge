#!/usr/bin/env python
# coding: utf-8

# # Analyzing Financial Data Using Python

# In[1]:


# Import os and cvs module / Dependencies
import os
import csv

# Set path for the file import and export
csvpath = os.path.join("budget_data.csv")
# print(csvpath)

file_to_output = os.path.join("pybank_financial_analysis_Michelle_Handipranata.txt")


# In[2]:


# Track the parameters
total_months = 0
month_of_change = []
profit_change_list = []
max_increase = ["", 0]
max_decrease = ["", 9999999999999999999999999]
total_profit = 0


# In[3]:


# Open csv and read the data
with open(csvpath, newline= "") as csv_budget:
    budget_reader = csv.reader(csv_budget, delimiter = ",")
    # print(budget_reader)
    
    # We want to skip the header
    budget_header = next(budget_reader)
    # print(budget_header)
    
    # Extract the value in the first row
    first_row = next(budget_reader)
    # print(first_row)
    
    total_months = total_months + 1
    
    total_profit = total_profit + int(first_row[1])
    prev_profit = int(first_row[1])
    # print(total_profit)
    # print(prev_profit)
    
    # Read each row after the header
    for data in budget_reader:
        
        # Calculate the total months
        total_months = total_months + 1
        
        # Calculate the total profit/losses
        total_profit = total_profit + int(data[1])
        # print(total_profit)
        
        # Calculate the change of profit/losses
        profit_change = int(data[1]) - prev_profit
        prev_profit = int(data[1])
        
        # Track the change of profit/losses
        # profit_change_list = profit_change_list + [profit_change]
        profit_change_list.append(profit_change)
            
        # Track the change of Month
        # month_of_change = month_of_change + [data[0]]
        date = data[0]
        month_of_change.append(date)
            
        if profit_change > max_increase[1]:
            max_increase[0] = data[0]
            max_increase[1] = profit_change
        
        if profit_change < max_decrease[1]:
            max_decrease[0] = data[0]
            max_decrease[1] = profit_change
            
    # Calculate the average of change in profit/losses
    profit_monthly_avg = sum(profit_change_list) / len(profit_change_list)
    
    # print(profit_monthly_avg)   
    # print(month_of_change)
    # print(profit_change_list)
    
with open(file_to_output, "w") as txt_file:
    
    output = (
            f"\nFinancial Analysis\n"
            f"==========================\n"
            f"Total Months: {total_months}\n"
            f"Total: ${total_profit}\n"
            f"Average Change: ${profit_monthly_avg:.2f}\n"
            f"Greatest Increase In Profits {max_increase[0]}, (${max_increase[1]})\n"
            f"Greatest Decrease In Profits {max_decrease[0]}, (${max_decrease[1]})\n"
    )
    
    print(output)
        
    # Save the result to the text file
    txt_file.write(output)
    


# In[ ]:





# In[ ]:




