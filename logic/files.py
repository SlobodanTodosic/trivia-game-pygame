import pandas as pd
import sqlite3 as sql
from matplotlib import pyplot as plt
from entity.player import Player
from entity.question import Question


# Function to extract questions from the text file
def process_trivia_file(filename):
    questions = []
    with open(filename, 'r', encoding='utf-8') as file:  # Opening the file
        for line in file:
            parts = line.strip().split(" - ")  # Return list with questions and answers
            print(parts[1])
            # Appending the questions list with Questions objects
            questions.append(Question(parts[0], parts[1], [parts[2], parts[3], parts[4]]))

    return questions


def create_connection(filename):
    conn = sql.connect(filename)  # Connecting with database
    c = conn.cursor()
    try: # Try to create nwe table in database
        c.execute("""CREATE TABLE scores(
                                          name text,
                                          score integer
                                          )""")
    except sql.OperationalError:
        print('Table already exist!')
    return conn


def save_score(player, filename):
    conn = create_connection(filename) # Get connection with database
    query = "SELECT * FROM scores"
    try:
        df = pd.read_sql(query, conn)  # Read sql to create DataFrame
    except sql.OperationalError:
        df = pd.DataFrame(columns=["name", "score"]) # If no data in base, create DataFrame with columns

    new_entry = pd.DataFrame({ # New entry for DataFrame with player name and scores
        "name": [player.name],
        "score": [player.score]
    })

    df = pd.concat([df, new_entry], ignore_index=True) # Add new entry to DataFrame
    df.to_sql('scores', conn, if_exists="replace", index=False) # Overwrite new DataFrame to database

    conn.close() # Close connection


def read_scores(filename):
    conn = create_connection(filename) # Get connection with database

    query = "SELECT * FROM scores"
    df = pd.read_sql(query, conn) # Read sql to create DataFrame

    players_names = df.iloc[:, 0] # Fetch player names from DataFrame
    players_scores = df.iloc[:, 1] # Fetch player scores from DataFrame
    scores = list(zip(players_names, players_scores)) # Creates zip list of combined data (player names, player scores)
    conn.close() # Close connection
    return scores

# Try to make plot work... unsuccessful

# def create_graph(highscores):
#     fig, axs = plt.subplots(figsize=(6, 8))
#     highscores.reverse()
#     names = [data[0] for data in highscores]
#     scores = [int(data[1]) for data in highscores]
#
#     axs.barh(range(10), scores, color='green', edgecolor='black', height=0.9)
#     for i, value in enumerate(names):
#         axs.text(1, i, f"{10 - i}. {value}", va = 'center', fontsize=12, color='black', fontweight='bold')
#     axs.set_xlim(0.0, scores[len(scores) - 1])
#     axs.set_yticklabels('')
#     axs.set_xlabel("Highscores")
#     fig.tight_layout()
#     plt.savefig('files/highscores.png', format="png", dpi=300)
#     plt.close(fig)
