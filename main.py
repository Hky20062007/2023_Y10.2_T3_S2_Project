# Kingsley
# ~~~~ Library App ~~~~
#
# Scan book ISBN
# If the book is loaned out then return it
# Display Book Details
# Scan Member ID
# Display Member details
# Get the rate
#
# Add 7 days to date as Duedate
# Add Date, Duedate, Book ISBN and Member ID to loan table
# 
# Display a message eg.Duedate
#
# Returning a book:
#      Get the date
#      Find the loan ID where the number ID and the book ISBN is and not returned
#      Input the returndate into the loan table

import datetime 
import sqlite3

DBFILE="Library.db"


def Scan_MemberID():
    return pass
# scan the card
member_id = int(input())
print(member_id)
#find the id in the Memberstable
#Display user details

def Scan_ISBN():
        ''' scan the book isbn '''
        #no idea how do we are going to do this
        isbn=0
        return isbn

def Return_the_book():
    ''' Return the loaned book to inventory '''
     #send the ISBN to be searched in the Loantable
     # Mark book as returned if it exists
     # Else ask the user to scan the numberID 
 try:
         squilConncettion = sqlite3.connect('sql.db')
         cursor = sqliteConnection.cursor()
         query = 'SELECT * from LoanTable Where isbn={isbn} and borrowdate=NULL'
         cursor.execute(query)
         result = cursor.fetchone()[2]
         cursor.close()
 except sqlite3.Error as error:
         print('Error occured-',error)
     finually:
         if squilConncettion:
           squilConncettion.close()
 return result

def get_date(): 
        ''' Get the current date and time '''
        thedate = datetime.datetime.now().strftime("%Y%m%d")
        print(thedate)
        return thedate
        

def Calc_DueDate(thedate):
    duedate = thedate + datetime.timedelta(days=7) 
    duedate = duedate.strftime("%Y%m%d")
    print(duedate)
    return duedate

def loan_book(isbn,member_id,borrowdate,duedate):
      ''' save details in database'''

      return "success"


def The_Secret_Sauce():
      ''' runs all of the other functions in the correct order '''
      bookisbn = Scan_ISBN()
      # check if book is loaned out
      # if not
      memberid = Scan_MemberID()
      borrowdate = get_date()
      duedate = Calc_DueDate()
      loan_book(bookisbn, memberid, borrowdate, duedate)

The_Secret_Sauce()
