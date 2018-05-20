import sqlite3

"""
Finger numbers:
thumb: 1
index: 2
middle: 3
ring: 4
pinky: 5
"""
def start(dbname):
    n = "user" + dbname + ".db"
    conn = sqlite3.connect(dbname + ".db")
    c = conn.cursor()

    try:
        c.execute("""CREATE TABLE fproximal1 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c.execute("""CREATE TABLE fproximal2 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c.execute("""CREATE TABLE fproximal3 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c.execute("""CREATE TABLE fproximal4 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c.execute("""CREATE TABLE fproximal5 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c.execute("""CREATE TABLE fdistal1 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c.execute("""CREATE TABLE fdistal2 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c.execute("""CREATE TABLE fdistal3 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c.execute("""CREATE TABLE fdistal4 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c.execute("""CREATE TABLE fdistal5 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()

    
    conn2 = sqlite3.connect(n)
    c2 = conn2.cursor()

    try:
        c2.execute("""CREATE TABLE proximal1 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c2.execute("""CREATE TABLE proximal2 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c2.execute("""CREATE TABLE proximal3 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c2.execute("""CREATE TABLE proximal4 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c2.execute("""CREATE TABLE proximal5 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c2.execute("""CREATE TABLE distal1 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c2.execute("""CREATE TABLE distal2 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c2.execute("""CREATE TABLE distal3 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c2.execute("""CREATE TABLE distal4 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")

        c2.execute("""CREATE TABLE distal5 (
                    xcoord real,
                    ycoord real,
                    zcoord real,
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    )""")
        
    except sqlite3.OperationalError:
        pass

    conn2.commit()
    conn2.close()

