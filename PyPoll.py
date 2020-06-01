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
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
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

#Save the results to our text file:
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    #save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate in candidate_votes:
        #Retrieve vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
            
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    #Print the winning candidate results
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning vandidate results to text file
    txt_file.write(winning_candidate_summary)

# Close the file.
election_data.close()
