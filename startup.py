import sqlite3
#LETS ASSUME THEY ALL LIVE ON THE SAME STREET

def firstSetUp():
    neigh_list = [
    ("John", "Gotti", 2),
    ("Mark", "Cuban", 4),
    ("Juan", "Perez", 6),
    ("Julian", "De", 8),
    ("Joe", "Rogan", 9),
    ("Tim", "Pool", 10),
]
    connection = sqlite3.connect('neighbours.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS neighbours (first_name, last_name, door_number)")
    connection.commit()
    cursor.executemany("INSERT INTO neighbours values (?,?,?)", neigh_list)
    res = cursor.fetchall()
    print(res)


def Read(query="SELECT first_name FROM neighbours"):
    connection = sqlite3.connect('neighbours.db')
    cursor = connection.cursor()
    res = cursor.execute(query)
    response = res.fetchall()
    print(response)
    connection.close()

# firstSetUp()
Read()