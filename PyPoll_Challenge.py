#Add our dependencies
import csv
import os

#Create a list manually to see if you remember the earlier part of the assignment
my_list = ["Jefferson", "Denver", "Arapahoe"]
print(my_list)

#Create a dictionary where the county is the key and the vote cast for each county in the election are the values
Dict = dict({'Jefferson': 38855, 'Denver': 306055, 'Arapahoe': 24801})

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter which will be used to determine the total number of votes cast.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# County options and votes
county_options = []
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
win_count = 0
win_perc = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name and county from each row
        candidate_name = row[2]
        county = row[1]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1

        #Replicate previous IF forumula for County
        if county not in county_options:
            # Add to the list of counties
            county_options.append(county)

            #Track county count
            county_votes[county] = 0

        #Add vote to county count
        county_votes[county] +=1

#Save the results to our text file:
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal + Adding Space & County Votes for Challenge
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")

    #save the final vote count to the text file.
    txt_file.write(election_results)
    
    for county in county_votes:
        #Retrieve vote count per county
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes)*100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

        print(county_results)
        txt_file.write(county_results)

        if(votes > winning_count) and (vote_percentage > winning_percentage):
            win_count = votes
            win_perc = vote_percentage
            winning_county = county
    
    #Print the winning county results
    winning_county_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary, end="")

    # Save the winning vandidate results to text file
    txt_file.write(winning_county_summary)
    
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