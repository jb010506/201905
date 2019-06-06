import sqlite3

def survey():
    name = input("What is your name?\n")
    age = input("How old are you?\n")
    ans = input("Hi, " + name + " ! Which is your favorite cellphone brand?\n"
                "(a) iPhone\n(b) Samsung\n(c) HTC\n(d) Huawei\n"
                )
    print("Thanks for your completion, your answer is \"" + ans + "\"\n")
    records = (name,age,ans)
    return records

class DB:
    def __init__(self, name):
        self.db_name = name
        
    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        print("Connection Successful")
        
    def create_table(self):
        self.conn.cursor().execute('''CREATE TABLE survey
           (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
           NAME  TEXT    NOT NULL,
           AGE   INT     NOT NULL,
           ANS   TEXT );''')
        print("Table created successfully");
        self.conn.commit()

    def add(self, records):
        c = self.conn.cursor()
        c.execute("INSERT INTO survey (NAME,AGE,ANS) \
              VALUES (?,?,?)", records);
        self.conn.commit()

    def print_data(self):
        cursor = self.conn.cursor().execute("SELECT id, name, age, ans from survey")
        for row in cursor:
           print ("ID = ", row[0])
           print ("NAME = ", row[1])
           print ("AGE = ", row[2])
           print ("ANS = ", row[3], "\n")

    def delete(self):
        selfconn.cursor().execute("DELETE from survey;")
        self.conn.commit()


if __name__ == "__main__":
    records=survey()
    db = DB('records.db')
    db.connect()
    #db.create_table()
    db.add(records)
    db.print_data()
