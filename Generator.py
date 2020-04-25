import sqlite3

import tkinter as tk
from tkinter import Tk, simpledialog
from tkinter.filedialog import askopenfilename

root = tk.Tk()
database_name = simpledialog.askstring(title="Database Name", prompt="Enter the Database name")

# Establish Connection to DB and Cursor
conn = sqlite3.connect(database_name)
connection = conn.cursor()

# Create Table
connection.execute('''CREATE TABLE english_words
        (word text, length int)''')

# Prompt user for filename
Tk().withdraw()
filename = askopenfilename()

# Loop over contents of file (Words)
with open(filename) as file:
    for line in file:
        word = line.strip().upper()
        length = len(word)

        # Commit words to DB
        statement = """INSERT INTO english_words VALUES ('{}', '{}')""".format(word, length)
        connection.execute(statement)

file.close()    # Close file
conn.commit()   # Commit saves to DB
conn.close()    # Close connection to DB

