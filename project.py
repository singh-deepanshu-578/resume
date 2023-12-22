import matplotlib.pyplot as pl
def show():
     import mysql.connector as ms
     db=ms.connect(host='127.0.0.1',port=3307,user='root',password='63426684',database='movtkt')
     crs=db.cursor()
     db.autocommit=True
     q='use movtkt'
     crs.execute(q)
     a='select * from mt'
     crs.execute(a)
     b=crs.fetchall()
     df=pd.DataFrame(b,columns=["m_code","m_name","showDate","showTiming"])
     print("DETAILS OF THE MOVIES ARE :")
     print()
     print(df)
     crs.close()
     input("Press any key to continue.....")
     admin()

def add():
     import mysql.connector as ms
     db=ms.connect(host='127.0.0.1',port=3307,user='root',password='63426684',database='movtkt')
     crs=db.cursor()
     db.autocommit=True
     q="use movtkt"
     crs.execute(q)
     m_code=int(input("Enter movie code:"))
     m_name=input("Enter movie name:")
     showDate=input("Enter date of the show in the format 'YYYY-MM-DD':")
     showTiming=input("Enter timing of the show in the format 'HH:MM:SS':")
     a="INSERT INTO mt values(%s,%s,%s,%s)"
     data=(m_code,m_name,showDate,showTiming)
     crs.execute(a,data)
     print()
     print(crs.rowcount, "record inserted")
     print("***** RECORD INSERTED SUCCESSFULLY*****")
     crs.close()
     input("Press any key to continue.....")
     admin()
def delete():
     import mysql.connector

     mydb=mysql.connector.connect(host='127.0.0.1',user='root',password="63426684",database='movtkt')
     crs=mydb.cursor()
     mydb.autocommit=True
     queryuse="use movtkt"
     crs.execute(queryuse)
     m_code=int(input('Enter Movie Code.: '))
     crs.execute('DELETE from mt where m_code=(%s)',(m_code,))
     print()
     print(crs.rowcount, "record deleted.")
     print(' ***Record Deleted Successfully***')
     crs.close()
     input("Press any key to Conti.....")
     admin()
def show_all():
     import mysql.connector as msc
     mydb=msc.connect(host='127.0.0.1',user='root',passwd='63426684',database='movtkt')
     crs=mydb.cursor()
     mydb.autocommit=True
     crs.execute("use movtkt")
     qry="Select * from bookings"

     crs.execute(qry)
     data1 = crs.fetchall() 
     df = pd.DataFrame(data1,columns=["b_code","name","address","phone","m_code","m_name","nt"])
     print(df)
     close()
     input("Press any key to Conti.....")
     admin()
def linegraph():
     df=pd.read_csv("bookings.csv")
     m_name=df["m_name"]
     nt=df["nt"]
     pl.xlabel("m_name")
     pl.ylabel("nt")
     pl.title("Tickets sold ")
     pl.plot(m_name,nt,linewidth=2,color='k',linestyle='solid',marker='o',markersize=5,markeredgecolor='red')
     pl.show()
     input("press any key to continue.....")
     graph()

def bargraph():
     df=pd.read_csv("bookings.csv")
     x=df["m_name"]
     y=df["nt"]
     pl.xlabel("movie name")
     pl.ylabel("number of tickets sold")
     pl.title("Tickets sold ")
     pl.bar(x,y,color=['red','b','g','k','m','c'])
     pl.show()
     input("press any key to continue.....")
     graph()
def graph():
     print("""
     1. Line Graph
     2. Bar Graph
     3. Back
     4. Main Menu
     """)
     e=int(input("Enter Choice:"))
     if e==1:
         linegraph()
     elif e==2:
         bargraph()
     elif e==3:
         admin()
     elif e==4:
         main()
     else:
         print("INVALID CHOICE")
         input("PRESS ANY KEY TO CONTINUE.....")
     graph()

def see():
     import mysql.connector as ms
     db=ms.connect(host='127.0.0.1',port=3307,user='root',password='63426684',database='movtkt')
     crs=db.cursor()
     db.autocommit=True
     q="use movtkt"
     crs.execute(q)
     b_code=int(input("Enter customer id"))
     crs.execute("Select * from bookings where b_code=(%s)",(b_code,))
     data=crs.fetchall()
     a=[]
     for i in data:
         a.append(i)

     if len(a)!=1:
         print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
         print()
         input("Press any key to continue.....")
         user()
     else:
         crs=db.cursor()
         db.autocommit=True
         q='use movtkt'
         crs.execute(q)
         crs.execute("Select * from bookings where b_code=(%s)",(b_code,))
         b=crs.fetchall()
         df=pd.DataFrame(b,columns=["b_code","name","address","phone","b_code","b_name","nt"])
         print("DETAILS OF YOUR TICKET IS:")
         print()
         print(df)
         crs.close()
         input("Press any key to continue.....")
         user()
     return("")
     crs.close()
     input("Press any key to continue.....")
     user()

def book():
     import mysql.connector as ms
     db=ms.connect(host='127.0.0.1',port=3307,user='root',password='63426684',database='movtkt')
     crs=db.cursor()
     db.autocommit=True
     q="use movtkt"
     crs.execute(q)
     m_name=input("Enter movie name")
     m_code=int(input("Enter movie code"))
     b_code=int(input("Enter customer code"))
     name=input("Enter your name")
     add=input("Enter your address")
     ph=input("Enter your phone no.")
     nt=int(input("Enter no. of tickets"))
     a="INSERT INTO bookings values(%s,%s,%s,%s,%s,%s,%s)"
     data=(b_code,name,add,ph,m_code,m_name,nt)
     crs.execute(a,data)
     print()
     print(crs.rowcount, "ticket booked")
     print("***** TICKET BOOKED SUCCESSFULLY")
     crs.close()
     input("Press any key to continue.....")
     user()
def dele():
     import mysql.connector
     mydb=mysql.connector.connect(host='127.0.0.1',port=3307,user='root',password='63426684',database='movtkt')
     crs=mydb.cursor()
     mydb.autocommit=True
     queryuse="use movtkt"
     crs.execute(queryuse)
     b_code=int(input('Enter Booking Code.: '))
     crs.execute('DELETE from bookings where b_code=(%s)',(b_code,))
     print()
     print(crs.rowcount, "record deleted.")
     print(' ***Record Deleted Successfully***')
     crs.close()
     input("Press any key to Conti.....")
     user()
def admin():
     print("""

     1. Show list of all movies
     2. Add new movie
     3. Delete a movie
     4. Show booked tickets
     5. Show Graph
     6. Main Menu
     7. Exit
     """)
     d=int(input("ENTER YOUR CHOICE:"))
     if d==1:
         show()
     if d==2:
         add()
     if d==3:
         delete()
     if d==4:
         show_all()
     if d==5:
         graph()
     if d==6:
         main()
     if d==7:
         exit()
     else:
         print("INVALID CHOICE")
         print()
         input("Press any key to continue.....")
         admin()
def user():
     print("""
     1. See your ticket
     2. Book a new ticket
     3. Delete a ticket
     4. Main Menu
     5. Exit
     """)
     ch=int(input("Enter your choice:"))
     if ch==1:
         see()
     elif ch==2:
         book()
     elif ch==3:
         dele()
     elif ch==4:
         main()
     elif ch==5:
         exit()
     else:
         print("CHOICE OUT OF RANGE")
         print()
         input("Press any key to continue.....")
         user()


def main():
     print("---------*MOVIE TICKET MANAGEMENT SYSTEM*---------")
     print()
     a=input("""
     1. Admin portal
     2. User portal
     """)
     if a=='1':
         b='web@portal'
         c=input("Enter admin password:")
         if(c=='web@portal'):
             admin()
         else:
             print("INVALID LOGIN CREDENTIALS FOR ADMIN")
             print()
             input("Press any key to continue")
             main()
     elif a=='2':
         user()
     else:
         print("CHOICE OUT OF RANGE")
         print()
         input("Press any key to continue.....")
         main()


while True:
     passw=input("ENTER PIN:")
     if passw=="634237":
         import mysql.connector as msc
         import datetime
         import pandas as pd
         import matplotlib.pyplot as pl
         db=msc.connect(host='127.0.0.1',port=3307,user='root',password='63426684')
         crs=db.cursor()
         db.autocommit=True
         q1="create database if not exists movtkt"
         crs.execute(q1)
         q2='use movtkt'
         crs.execute(q2)
         q3='create table if not exists mt(m_code int not null primary key, m_name varchar(20) not null unique, showDate date not null, showTiming varchar(20) not null)'
         crs.execute(q3)
         crs.execute("SELECT * FROM mt")
         crs.fetchall()
         rc=crs.rowcount
         if rc==0:
             qi1="insert into mt values(101,'Ram Setu','2022-12-27','10:00:00')"
             qi2="insert into mt values(102,'Major', '2022-12-27','10:00:00')"
             qi3="insert into mt values(103,'Jersey', '2022-12-27','10:00:00')"
             qi4="insert into mt values(104,'KGF:Chapter 2','2022-12-27','10:00:00')"
             qi5="insert into mt values(105,'The Kashmir Files','2022-12-27','10:00:00')"
             qi6="insert into mt values(106,'Tadap', '2022-12-27','10:00:00')"
             qi7="insert into mt values(107,'Runway 34', '2022-12-27','10:00:00')"
             crs.execute(qi1)
             crs.execute(qi2)
             crs.execute(qi3)
             crs.execute(qi4)
             crs.execute(qi5)
             crs.execute(qi6)
             crs.execute(qi7)
         crs.execute(q2)
         q4='create table if not exists bookings(b_code int not null primary key auto_increment, name varchar(20) not null, address varchar(20), phone bigint, m_code int, m_name varchar(20), no_of_tickets int)'
         crs.execute(q4)
         crs.execute("SELECT * FROM bookings")
         crs.fetchall()
         r=crs.rowcount
         if r==0:
             qi8="insert into bookings values(001,'Ayush', 'Delhi','9856235416',102,'Major',15)"
             qi9="insert into bookings values(002,'Ansh', 'Delhi','8569654125',103,'Jersey',16)"
             qi10="insert into bookings values(003,'Aryan','Agra','9658745210',104,'KGF:Chapter 2',16)"
             qi11="insert into bookings values(004,'Arjun','Lucknow','9235689745',105,'The Kashmir Files',18)"
             qi12="insert into bookings values(005,'Kanchan','Meerut','9658523652',106,'Tadap',8)"
             qi13="insert into bookings values(006,'Manvi','Ludhiana','8595231746',107,'Runway 34',9)"
             qi14="insert into bookings values(007,'Rahul','Amritsar','8596325412',107,'Runway 34',13)"
             crs.execute(qi8)
             crs.execute(qi9)
             crs.execute(qi10)
             crs.execute(qi11)
             crs.execute(qi12)
             crs.execute(qi13)
             crs.execute(qi14)
         crs.close()
         print("---------*WELCOME TO MOVIE TICKET MANAGEMENT SYSTEM*---------")
         print()
         print()
         main()
     else:
         print("WRONG PIN")
         print()
         print()
         retry=input("Do you want to retry? Y or N")
         if retry=='Y' or retry=='y':
             continue
         else:
             print("!!You chose not to continue!!")
             break 
