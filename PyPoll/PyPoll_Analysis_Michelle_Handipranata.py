#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import os and cvs module / Dependencies
import os
import csv

# Set path for the file import and export
csvpath = os.path.join("election_data.csv")
# print(csvpath)

file_to_output = os.path.join("election_analysis_Michelle_Handipranata.txt")


# In[2]:


# Set the parameters
total_votes = 0
candidate_list = []

# candidate votes is a dictionary
candidate_votes = {}

winning_candidate = ""
winning_count = 0


# In[3]:


# Open csv and read the data
with open(csvpath, newline = "") as csv_election:
    election_reader = csv.reader(csv_election, delimiter = ",")
    # print(election_reader)
    
    # Read the header
    election_header = next(election_reader)
    # print(election_header)
    
    # Read each row
    for election_row in election_reader:
        
        # Calculate total votes
        total_votes = total_votes + 1
        
        # Extract candidate name from each row
        candidate_name = election_row[2]
        
        # If statement for different candidate on the next row
        if candidate_name not in candidate_list:
            
            # Add it to the candidate name list
            candidate_list.append(candidate_name)
            
            # Start tracking the candidate voter count which starts from 0
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        
with open(file_to_output, "w") as txt_file:
    
    # Print the total votes count
    election_results = (
        f"Election Results\n"
        f"-------------------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------------------------\n"
    )
    
    # print(election_results, end = "")
    
    # Save the final votes count to the text file
    txt_file.write(election_results)
    
    # Determine the winner 
    for candidate in candidate_votes:
        
        # Retrieve votes count and Calculate percentages
        votes = candidate_votes.get(candidate)
        votes_percentage = float(votes) / float(total_votes) * 100
        
        # Determine winning votes count and candidate name
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
            
        # Print each candidate's votes count and percentage
        votes_results = (
            f"{candidate} : {votes_percentage:.3f}% ({votes})\n"
        )
    
        # print(votes_results, end = "")
        
        # Save each candidate's votes count and percentage to text file
        txt_file.write(votes_results)
        
    # Print the winner
    winning_candidate_results = (
        f"-------------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------------------------\n"
    )
    # print(winning_candidate_results, end = "")
    
    # Save the winner result to the text file
    txt_file.write(winning_candidate_results)
    


# In[ ]:




