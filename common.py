import psycopg2
from pprint import pprint as pp
from prettytable import PrettyTable

import re

def c(s):
<<<<<<< HEAD
    return re.sub(r'\s+', ', ', s)

=======
    return re.sub('\s+', ', ', s)
>>>>>>> 34aa304 (lots of us)

def show_table(rows, cols='', ncols=None):
    if ncols != None:
        cols = [('c%d' % i) for i in range(1, ncols+1)]
    else:
        cols = cols.split()
    table = PrettyTable( cols )
    table.add_rows(rows)
    print(table)


SHOW_CMD = True

def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

conn = psycopg2.connect(database='trax', user='isdb')
conn.autocommit = True
cur = conn.cursor()


