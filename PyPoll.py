import csv
import os
file_to_load = os.path.join ("Resources","election_results.csv")
file_to_save = os.path.join ("analysis","election_analysis.txt")
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
  file_reader = csv.reader(election_data)
  headers = next(file_reader)
  for line in file_reader:
        # Add to the total vote count.
        total_votes = total_votes+1
        # Get the candidate name from each row.
        candidate_name = line[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+= 1  
        # Save the results to our text file.
      
             
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes=candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        candidate_results = (
             f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
     #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

#print(winning_candidate_summary)
        





    


 