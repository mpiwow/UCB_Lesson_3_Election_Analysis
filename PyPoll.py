#The data we need to retrieve has to answer the following:
# 1) The total number of votes cast
# 2) A complete list of candidates who received votes
# 3) The percentage of votes each candidate won
# 4) The total number of votes each candidate won
# 5) The winner of the election based on popular vote

#Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter which will be used to determine the total number of votes cast.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []

#Declare the empty dictionary.
candidate_votes = {}

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1

        #Print the candidate vote dictionary
        print(candidate_votes)

        # Winning Candidate and Winning Count Tracker
        winning_candidate = ""
        winning_count = 0
        winning_percentage = 0

        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
        for candidate in candidate_votes:
            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate]
            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            # 4. Print the candidate name, vote count, and percentage of votes

            # Determine winning vote count and candidate
            # 1. Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent = vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # 3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate  
            
            print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)

# To do: perform analysis
   
# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    
    # Write some data to the file.
    #txt_file.write("Hello World")

# Close the file.
election_data.close()
