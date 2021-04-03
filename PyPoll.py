# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes 
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import the datetime class from the datatime module 
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

# Open the election results and read the file
# election_data = open(file_to_load, 'r')
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
        print(row)

# Close the file
# election_data.close()


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



