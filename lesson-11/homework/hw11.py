#task1
import sqlite3
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")
cursor.executemany("""
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])
conn.commit()
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")
conn.commit()
cursor.execute("""
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
""")
print("Bajoran Characters:", cursor.fetchall())
cursor.execute("""
DELETE FROM Roster WHERE Age > 100
""")
conn.commit()
cursor.execute("""
ALTER TABLE Roster ADD COLUMN Rank TEXT
""")
cursor.executemany("""
UPDATE Roster SET Rank = ? WHERE Name = ?
""", [
    ("Captain", "Benjamin Sisko"),
    ("Lieutenant", "Ezri Dax"),
    ("Major", "Kira Nerys")
])
conn.commit()
cursor.execute("""
SELECT * FROM Roster ORDER BY Age DESC
""")
print("Characters sorted by Age :", cursor.fetchall())
conn.close()

#task2
import sqlite3
conn = sqlite3.connect("library.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")
cursor.executemany("""
INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)
""", [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
])
conn.commit()
cursor.execute("""
UPDATE Books
SET Year_Published = 1950
WHERE Title = '1984'
""")
conn.commit()
cursor.execute("""
SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'
""")
print("Dystopian Books:", cursor.fetchall())
cursor.execute("""
DELETE FROM Books WHERE Year_Published < 1950
""")
conn.commit()
cursor.execute("""
ALTER TABLE Books ADD COLUMN Rating REAL
""")
cursor.executemany("""
UPDATE Books SET Rating = ? WHERE Title = ?
""", [
    (4.8, "To Kill a Mockingbird"),
    (4.7, "1984"),
    (4.5, "The Great Gatsby")
])
conn.commit()
cursor.execute("""
SELECT * FROM Books ORDER BY Year_Published ASC
""")
print("Books sorted by Year Published :", cursor.fetchall())
conn.close()
