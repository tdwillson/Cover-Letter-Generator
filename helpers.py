import sqlite3

def letter_dict():
    letters = []
    db = sqlite3.connect("letters.db")
    c = db.cursor()
    c.execute("SELECT * FROM letters")
    out = c.fetchall()
    for row in out:
        letter = {
            'id' : row[0],
            'company' : row[1],
            'position' : row[2],
            'addon' : row[3]
        }
        letters.append(letter)
    return letters