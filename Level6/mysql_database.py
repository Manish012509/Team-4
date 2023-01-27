import mysql.connector
from Level1.FileFinder import FileFinder
import Level1.file_ui

class Mysql_DBaccess:
    def __init__(self,host,user,password,db):
        self.host=host
        self.user=user
        self.password=password
        self.db=db
        try:
            self.connection=mysql.connector.connect(host=self.host,database=self.db,
                                                    user=self.user,
                                                    password=self.password)
        except:
            print("Error while connecting to the database")
    def inser_data(self,filename):
        self.filename=filename
        self.cur=self.connection.cursor()
        sql='insert into files(filename) values(%s);'
        val=(self.filename) #To pass the values as a tuple(Immutable)
        self.cur.execute(sql,(val,))
        self.connection.commit()
    def search(self):
        self.cur = self.connection.cursor()
        sql="SELECT *FROM files limit 0,10"
        data=self.cur.execute(sql)
        data=self.cur.fetchall()
        return data
    def searchDB(self,fil):
        self.cur = self.connection.cursor()

        #self.f="filename"
        sql="select *from files where filename like '%{0}'".format(fil)
        self.cur.execute(sql)
        row= self.cur.fetchone()
        if row==None:
            print(0)
        else:
            print(row)
    def findfile(self):
        filename = input("Enter the file name:")
        path = input("Enter the Dick to find:")
        self.cur = self.connection.cursor()
        sql="select * from file where filename like '%{0}'".format(filename)
        self.cur.execute(sql)
        row=self.cur.fetchone()
        if row!=None:
            print(row)
        else:
            obj=FileFinder()
            obj.find_file(filename,path)
        print("File searching in the directory")






dbobj=Mysql_DBaccess('localhost','root','Manish@123','searchfiles')
dbobj.inser_data('C:\\hcl\\hcl.txt')
#dbobj.inser_data('Hello')
#dbobj.searchDB('Hello')
#dbobj.searchDB('C:\\hcl\\hcl.txt')
#dbobj.inser_data('C://hcl//hcl.txt')
#dbobj.searchDB('C://hcl//hcl.txt')
#dbobj.searchDB("\\\hcl.txt")
dbobj.findfile()


