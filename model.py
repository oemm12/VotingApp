import csv

VOTES_FILE = "votes.csv"


def save_vote(candidate: str) -> bool:
    '''saves the vote to the csv'''
    try:
        with open(VOTES_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([candidate])
        return True
    except Exception as e:
        print(f"couldn't save: {e}")
        return False


def get_vote_counts() -> dict[str, int]:
    '''reads the csv and returns the counts'''
    counts = {"John": 0, "Jane": 0}
    try:
        with open(VOTES_FILE, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] in counts:
                    counts[row[0]] += 1
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f" reading issue: {e}")
    return counts
