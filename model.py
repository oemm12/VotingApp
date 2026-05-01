import csv
import os

VOTES_FILE = "votes.csv"


def save_vote(candidate):
    '''Saves a vote for the selected individual (John or Jane) to the CSV file.'''
    try:
        with open(VOTES_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([candidate])
        return True
    except Exception as e:
        print(f"Error saving vote: {e}")
        return False


def get_vote_counts():
    '''reades into the csv file and counts the votes for each individual'''
    counts = {"John": 0, "Jane": 0}
    if not os.path.exists(VOTES_FILE):
        return counts
    try:
        with open(VOTES_FILE, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] in counts:
                    counts[row[0]] += 1
    except Exception as e:
        print(f"Error reading votes: {e}")
    return counts
