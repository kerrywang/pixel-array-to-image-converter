import csv

def get_user_list(filename='./fer2013.csv'):
    """return list of user tuple. e.g. ('001,', 'demo1'), ('002,', 'demo2')]"""
    user_list = []
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            r = row[0].split(' ')
            user_list.append([float(x) for x in r])
    return user_list

