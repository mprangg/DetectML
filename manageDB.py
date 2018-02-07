
import sqlite3
def create_Table(nameDB,exeText):
    con = sqlite3.connect(nameDB)
    c = con.cursor()
    c.execute(exeText)
    #c.execute('''CREATE TABLE object_Train (name varchar(50) primary key,ID INTEGER primary key)''')

#>>>>>>>>>>>>>> INSERT Obj Train <<<<<<<<<<<<<<<<
def insert_object_Train(name,lenID):
    with sqlite3.connect("corpus_Obj.db") as con:
        try :
            con.execute("insert into object_Train values (?, ?)", (name, lenID)) #nameObj,ID = {PK}
        except :
            print "!!! DUPLICATE entry !!!"
            return "DUPLICATE"

#>>>>>>>>>>>>>> COUNT ROWs <<<<<<<<<<<<<<<<<<<<<<
def lenDB(nameDB,exeText):
    with sqlite3.connect(nameDB) as con:
        cur = con.cursor()
        cur.execute(exeText)
        rows = cur.fetchall()
        return len(rows)

        #print len(rows)
#>>>>>>>>>>>>> SEARCH obj TRAIN <<<<<<<<<<<<<<<<<<
def search_object_Train(name):
    with sqlite3.connect("corpus_Obj.db") as con:
        cur = con.cursor()
        #cur.execute('SELECT * FROM object_Train WHERE name=?',(name,))
        cur.execute("SELECT " + "ID" + " FROM object_Train where " + "name" + "=?", (name,))
        rows = cur.fetchone()
        for element in rows:
            return element

       # return cur.fetchone() # None OR (u'Ball', 2)

#>>>>>>>>>>>>>>>>JSON<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import pyodbc
import json
import collections

def Jtest():
    connection = sqlite3.connect('corpus_Obj.db')
    cursor = connection.cursor()
    query = "SELECT * FROM object_Train"
    result = cursor.execute(query)

    items2 = [dict(zip([key[0] for key in cursor.description], row)) for row in result]
    print (json.dumps({'items2': items2}))

    with open('JsonObj1.json', 'w') as outfile:
        json.dump(items2, outfile)
    # Convert query to objects of key-value pairs
"""
if __name__ == '__main__':
    #create_1()
    lenObj = int(lenDB("corpus_Obj.db","SELECT * FROM object_Train"))
    #print search_object_Train("all")
    A= "ball"
    #print lenObj
    #print insertObj_NameNum(A,lenObj)   #/// DUPLICATE or NONE

print search_object_Train("Ball")

"""

