#Any necessary imports
import os
import csv

#Assigns variable for read file
election_results = os.path.join('Resources','election_results.csv')
#Assigns variable for write file
election_save = os.path.join("analysis","election_analysis.txt")

#Declare Variables
total_vote = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open read file of election results
with open(election_results) as election_data:
    file_reader = csv.reader(election_data)

    #Get headers and go to next row
    headers = next(file_reader)

    for i in file_reader:
        #Save candidate name from each row
        candidate_name = i[2]

        #Add candidate name to list and add to candidates vote
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        #Add candidates votes
        candidate_votes[candidate_name] += 1

        #Total vote count
        total_vote += 1
    


#Loop through each canditate and calculate vote percentage
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]

    vote_percentage = float(votes) / float(total_vote) * 100

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
    #Finds winning candidate and percentage of votes
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n"
)

print(winning_candidate_summary)


#Writes to writable file
with open(election_save, "w") as txt_file:
    txt_file.write("Arapahoe\nDenver\nJefferson")


#-------------To dos-------------
#Total of votes cast
#A complete list of candidates
#Total number of votes each candidate recieved
#Percntage of votes each candidate won
#The winnder of the election based on popular vote
