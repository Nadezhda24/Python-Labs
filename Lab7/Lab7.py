import sqlite3

db = sqlite3.connect('Teacher.sqlite')
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Person (
    record        INT       PRIMARY KEY
                            UNIQUE,
    name          CHAR (30),
    first_name    CHAR (30),
    second_name   CHAR (30),
    birthday      DATE,
    telephone     CHAR (15),
    experience    INT,
    id_gender     INT,
    id_discipline INT
);''')
cur.execute('''CREATE TABLE  IF NOT EXISTS Gender (
    id_gender   INT       PRIMARY KEY
                          UNIQUE
                          REFERENCES Person (id_gender) ON DELETE NO ACTION
                                                        ON UPDATE NO ACTION,
    genden_name CHAR (10) 
);
''')
cur.execute('''CREATE TABLE IF NOT EXISTS Discipline (
    id_discipline   INT       PRIMARY KEY
                              REFERENCES Person (id_discipline) ON DELETE NO ACTION
                                                                ON UPDATE NO ACTION
                              UNIQUE,
    name_discipline CHAR (30) 
);
''')

Discipline = [(1, "math"), (2, "english"), (3, "python"), (4, "c++"), (5, "java")]
cur.executemany("INSERT INTO Discipline VALUES (?, ?)", Discipline)

cur.execute("SELECT * FROM Discipline where  id_discipline  = 1 ")
print(cur.fetchall())

Gender = [(1, "m"), (2, "w")]
cur.executemany("INSERT INTO Gender VALUES (?, ?)", Gender)

cur.execute("SELECT * FROM Gender")
print(cur.fetchall())

cur.execute("INSERT INTO Person VALUES (1, \"Person1\", \"Person1\", \"Person1\", \"12/12/12\", \"3556654\", 10,1,1 )")
cur.execute("SELECT * FROM Person")
print(cur.fetchall())

cur.execute("DELETE FROM Person where record = 1")
print(cur.fetchall())

