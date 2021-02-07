import csv
import time
import sys
import re
import subprocess

def get_following(username):
    cmd = "twint -u %s --following" % username
    result = subprocess.check_output(cmd, shell=True)
    names = result.splitlines()
    return names
    

infile = "writers_network.csv"
writer_data = open(infile)
csv_reader = csv.reader(writer_data)


OUTFILE = "writers_plus_twitter_network_final.csv"
output_file = open(OUTFILE, 'w')

keys = ['writer', 'twitter_name', 'num_followers', 'num_articles', 'gender', 'last_url', 'following']
dict_writer = csv.DictWriter(output_file, keys)
dict_writer.writeheader()

csv.field_size_limit(sys.maxsize)
for row in csv_reader:
    new_row = {}
    new_row["writer"] = row[0]
    new_row["twitter_name"] = row[1]
    new_row["num_followers"] = row[2]
    new_row["num_articles"] = row[3]
    new_row["gender"] = row[4]
    new_row["last_url"] = row[5]
    new_row["following"] = row[6]

    print(new_row["twitter_name"])

    if (new_row["following"] == ""):
        try:
            following = get_following(new_row["twitter_name"])
        except:
            print("missed user %s" % new_row["twitter_name"])
            continue
        new_row["following"] = ":".join(following)
        print(new_row["following"])

    dict_writer.writerow(new_row)
