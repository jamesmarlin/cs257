#James Marlin
#Did not have time to complete Medals
import psycopg2
import argparse

#Login information
from config import password
from config import database
from config import user

#Connects to database with login information
try:
    connection = psycopg2.connect(database=database, user=user, password=password)
except Exception as e:
    print(e)
    exit()
 
 #Arugments used for command line
def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-NOC','--NOC', metavar= 'S', type=str, nargs='+', help= "Using a S input, prints out a list of athletes from the given region") 
    parser.add_argument('-MEDAL','--medal',metavar= 'S',type=str, nargs='+', help="Using a S input, prints out a list of in descending order of medals from the specified NOC")
    parser.add_argument('-WEIGHT','--weight',metavar= 'S',type=str, nargs='+', help="Using a S input, prints out a list of athletes with the specified weight")

    return parser

# Prints error message
def has_arguments(args, parser):
    if (args.NOC is None and args.medal is None and args.weight is None):
        error = parser.parse_args(['-h'])
        print(error, file=sys.stderr)
        quit()

# Prints out the athlete based on the region 
def NOC_Find(args,parser):
    try:
        cursor = connection.cursor() 
        query = '''SELECT athletes_games.team, athletes.names
                    FROM athletes_games, athletes
                    WHERE athletes.id = athletes_games.athletes_id
        '''
        cursor.execute(query)
        print(cursor.query)
    except Exception as e:
        print(e)
        exit()

    if (args.NOC is not None):
        print('===== All Athletes from this Region =====')
        for row in cursor: 
            if args.NOC[0] == str(row[0]):
                print(str(row[1]))
    return args

# Prints out the NOC and all of the medals for that region
def Medal_find(args,parser):
    try:
        cursor = connection.cursor()
        query = '''SELECT COUNT(athletes_total.medal)
                    FROM athletes_total, athletes_games
                    GROUP BY athletes_games.NOC 
                    '''
        cursor.execute(query)

    except Exception as e:
        print(e)
        exit()
    
    if (args.medal is not None):
        print('===== All Medals for this Region =====')
        for row in cursor:
            print(row[1])
    return 

# Prints out all of the athletes with the typed weight
def Weight(args,parser):
    try:
        cursor = connection.cursor()
        query = 'SELECT weight, names FROM athletes'
        cursor.execute(query)

    except Exception as e:
        print(e)
        exit()
    
    if (args.weight is not None):
        print('===== Athlete with this Weight =====')
        for row in cursor:
            if int(args.weight[0]) == int(row[0]):
                print(str(row[1]))

    return args

def main():
    #creates the parser arguments 
    parser = build_parser()
    args = parser.parse_args()
    has_arguments(args, parser)

    #arguments for all inputs
    NOC_Find(args,parser)
    Medal_find(args,parser)
    Weight(args,parser)

if __name__ == '__main__':
    main()
    connection.close()
