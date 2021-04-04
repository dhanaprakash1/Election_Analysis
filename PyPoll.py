# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes 
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add Dependencies
import datetime as dt
import csv
import os

# Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()
#Print the present time 
print("The time right now is", now)

#Assign a variable for file to load and the path
#file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")
print(file_to_load)
# create a filename variable to a direct or indirect path to a file
file_to_save = os.path.join("analysis", "election_analysis.txt") 
print(file_to_save)

# Initialize a total vote counter
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
# Declare teh empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
# election_data = open(file_to_load, 'r')
# Close the file
# election_data.close()
with open(file_to_load) as election_data:
    # To do: perform analysis
    print(election_data)
    #Read the file object with tge reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

    #Print each row in teh CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # print(row)

        # Print the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list
        # If teh candidate does not match any existing candidate...candidate_options
        if candidate_name not in candidate_options:
            # Add itt to the list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking candidate vote count
            candidate_votes[candidate_name] = 0
        
        # Add a vote to the candidate_count
        candidate_votes[candidate_name] += 1

# Print teh candidate vote dictionary
print(candidate_votes)

# Print then candiadte list 
print(candidate_options)

# 3. Print the total votes
print(total_votes)

# Determine the percentage of votes for each candidate by looping through the count 
# Iterate through the candidate list
for candidate_name in candidate_votes:
    # Retrive vote count of a candidate 
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes 
    vote_percentage = float(votes) / float(total_votes) * 100

    #To do: print out each candidate's name, vote count and the percentage of votes to teh termoinal 
    print(f"{candidate_name}: {vote_percentage:1f}% ({votes:,})\n")

    # Determine winning count and candidate
    # Determine if the votes is greater than the winning count 
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # And set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name 

# To do: print out the winning candidate, vote count and percentage to the terminal
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n")
print(winning_candidate_summary)

# Using the open() function with the "w" mode we will write data to teh file
# outfile = open(file_to_save, "w")
with open(file_to_save, "w") as txt_file:
    # write some data to the file
    # outfile.write("Hello World")

    # Write three counties 
    txt_file.write("Counties in the Election")
    txt_file.write("Arapahoe\nDenver\nJefferson")
    #txt_file.write("Denver")
    #txt_file.write("Jefferson")
# Close the file to the file
# outfile.close()



