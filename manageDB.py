
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
        cur.execute('SELECT * FROM object_Train WHERE name=?',(name,))
        return cur.fetchone() # None OR (u'Ball', 2)

if __name__ == '__main__':
    #create_1()
    lenObj = int(lenDB("corpus_Obj.db","SELECT * FROM object_Train"))
    print search_object_Train("all")
    A= "ball"
    #print lenObj
    #print insertObj_NameNum(A,lenObj)   #/// DUPLICATE or NONE
