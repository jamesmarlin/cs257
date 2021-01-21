# Authors: Etienne Richart and James Marlin
# Revised by: Etienne Richart and James Marlin
# Using flags, you will find the author, name, and year of release of any book listed inside books.csv

import argparse
import csv
import sys

# Class of books to maintain a books, author, title and publication year
class Book:
    def __init__(self, title, year, author):
        self.author = author
        self.title = title
        self.year = int(year)
    def __str__(self):
        return(self.title + '; ' + self.author + '; ' + str(self.year))
        
# Create arguments for what the user will be searching - title, author, and years
def build_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-title', '--title', metavar ='S', type=str, nargs='+' , help= 'Given a search string S, print a list of books limitted by those whose titles contain S (case-insensitive)')
    parser.add_argument('-author', '--author', metavar = 'S', type=str, nargs='+', help='Given a search string S, print a list of authors whose names contain S (case-insensitive). For each such author, print a list of the author\'s books.')
    parser.add_argument('-year', '--year', metavar='Y',type=int, nargs=2, help='Given a range of years A to B, print a list of books published between years A and B, inclusive.')

    return parser

# Prints error message
def has_arguments(args, parser):
    if (args.year is None and args.title is None and args.author is None):
        error = parser.parse_args(['-h'])
        print(error, file=sys.stderr)
        quit()

# Goes through books.csv and splits each section to access arguments
def readin_csv():
    bookset = set()
    with open('books.csv', newline = '') as csvfile:
        bookreader = csv.reader(csvfile, delimiter =',', quotechar = '"')
        for row in bookreader:
            book = Book(row[0], row[1], row[2])
            bookset.add(book)
    return bookset

# Takes arguments and goes through csv to find a match
def filter_books(args, bookset):
    if (args.title is not None):
        title = ' '.join(st.strip().casefold() for st in args.title)
        temp = [book for book in bookset if title in book.title.casefold()]
        bookset = temp

    if (args.year is not None):
        start = min(args.year)
        end = max(args.year)
        temp = [book for book in bookset if book.year >= start and book.year <= end]
        bookset = temp    

    if (args.author is not None):
        author = ' '.join(st.strip().casefold() for st in args.author)
        auths = dict()
        for book in bookset:
            if author in book.author.casefold():
                if book.author in auths:
                    auths[book.author].append(book)
                else:
                    auths[book.author] = [book]
        bookset = auths

    return bookset

# Print the books that have passed the filtering
def print_matching_books(args, bookset):
    if (args.author is not None):
        for auth in bookset:
            print(auth)
            for entry in bookset[auth]:
                print('\t' + entry.title + '; ' + str(entry.year))
            print()
    else:
        for book in range(len(bookset)):
            print(bookset[book])

def main():
    # Creates a parser, reads in the arguments, throws an error if no arguments provided
    parser = build_parser()
    args = parser.parse_args()
    has_arguments(args, parser)
    
    # Reads-in a csv file, fills bookset with Book objects, then filters out books that don't match the arguments
    bookset = readin_csv()
    bookset = filter_books(args, bookset)
    print_matching_books(args, bookset)

if __name__ == '__main__':
    main()