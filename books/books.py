#created by Etienne Richart and James Marlin
#using flags, you will find the author, name, and year of release of any book listed inside books.csv

import argparse
import csv

parser = argparse.ArgumentParser()

parser.add_argument('-title', '--title', metavar ="S", type=str, nargs='+' ,help= "Given a search string S, print a list of books limitted by those whose titles contain S (case-insensitive)")
parser.add_argument('-author', '--author', metavar = "S", type=str, nargs='+',help="Given a search string S, print a list of authors whose names contain S (case-insensitive). For each such author, print a list of the author's books.")
parser.add_argument('-year', '--year', metavar="Y",type=int, nargs=2, help="Given a range of years A to B, print a list of books published between years A and B, inclusive.")

args = parser.parse_args()
 
if (args.year is None and args.title is None and args.author is None):
    error = parser.parse_args(['-h'])
    print(error)
    quit()

class Book:
    def __init__(self, title, year, author):
        self.author = author.casefold()
        self.title = title.casefold()
        self.year = int(year)
    def __str__(self):
        return(self.title + "; " + self.author + "; " + str(self.year))

bookset = set()

with open('books.csv',newline='') as csvfile:
    bookreader = csv.reader(csvfile, delimiter= ',', quotechar = '"')
    for row in bookreader:
        book = Book(row[0],row[1],row[2])
        bookset.add(book)

args = parser.parse_args()
if (args.title is not None):
    title = " ".join(st.strip().casefold() for st in args.title)
    temp = [x for x in bookset if title in x.title]
    bookset = temp

if (args.year is not None):
    start = min(args.year)
    end = max(args.year)
    temp = [x for x in bookset if x.year >= start and x.year <= end]
    bookset = temp    

if (args.author is not None):
    author = " ".join(st.strip().casefold() for st in args.author)
    auths = dict()
    for x in bookset:
        if author in x.author:
            if x.author in auths:
                auths[x.author].append(x)
            else:
                auths[x.author] = [x]
    for auth in auths:
        print(auth)
        for entry in auths[auth]:
            print("\t" + entry.title + "; " + str(entry.year))
        print()
else:
    for x in range(len(bookset)):
        print(bookset[x])

