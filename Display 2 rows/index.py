import venv
import pymongo
import sys

client = pymongo.MongoClient("mongodb://localhost:27017/") 

from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
import webbrowser

load_dotenv(find_dotenv())

password = os.environ.get("nhy6mju7")
username = "manager@spdevgroup.com"

connection_string = f"mongodb+srv://manager_db_user:iLjfKQn4vfaM5JX3@cluster0.ogjompv.mongodb.net/?appName=Cluster0"
client = MongoClient(connection_string)
book_db = client.Books
book_collection = book_db.Books_Read
printer = pprint.PrettyPrinter()

# SECTION 0
for book in book_collection.find():
  printer.pprint(book)       
  
  books = []

tbl="<tr><td>Book Title</td><td>First Name</td><td>Last Name</td><td>Summary</td></tr>"
books.append(tbl)

# SECTION 1
# part a
for book in book_collection.find_one({"_id": pymongo.ObjectId("692e18229b1e706ed49d6a5f")}):
    a = "<tr><td>%s</td>"%book['Book_Title']
    books.append(a)
    b = "<td>%s</td>"%book['First_Name']
    books.append(b)
    c = "<td>%s</td>"%book['Last_Name']
    books.append(c)
    d = "<td>%s</td></tr>"%book['Summary']
    books.append(d)
    #printer.pprint(book)


#part b
contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>News Site 1</title>
</head>
<body>
<table>
%s
</table>
</body>
</html>
'''%(books)

#part c
filename = 'index.html'

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)    
webbrowser.open(filename)

#END of SECTION 1-----------------------------------

#START oF SECTION 2
# part a
for book in book_collection.find():
    a = "<tr><td>%s</td>"%book['Book_Title']
    books.append(a)
    b = "<td>%s</td>"%book['First_Name']
    books.append(b)
    c = "<td>%s</td>"%book['Last_Name']
    books.append(c)
    d = "<td>%s</td></tr>"%book['Summary']
    books.append(d)
    #printer.pprint(book)


#part b
contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>News Site 1</title>
</head>
<body>
<table>
%s
</table>
</body>
</html>
'''%(books)

#part c
filename = 'index.html'

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)    
webbrowser.open(filename)