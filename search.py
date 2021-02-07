#https://github.com/ideoforms/python-twitter-examples/blob/master/twitter-user-search.py

from twitter import *
import csv
import time

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
import sys
sys.path.append(".")
import config

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

#-----------------------------------------------------------------------
# perform a user search 
# twitter API docs: https://dev.twitter.com/rest/reference/get/users/search
#-----------------------------------------------------------------------




infile = "writers_data_short.csv"
writer_data = open(infile)
csv_reader = csv.reader(writer_data)


OUTFILE = "writers_plus_twitter.csv"
output_file = open(OUTFILE, 'w')

keys = ['writer', 'twitter_name', 'num_articles', 'gender', "last_url"]
dict_writer = csv.DictWriter(output_file, keys)
dict_writer.writeheader()
for row in csv_reader:
    new_row = {}
    new_row["writer"] = row[0]
    new_row["num_articles"] = row[1]
    new_row["gender"] = row[2]
    new_row["last_url"] = row[3]

    results = twitter.users.search(q = new_row["writer"] )
    try:
        twitter_name = results[0]["screen_name"]
    except:
        print("missed %s" % new_row["writer"]) 
        continue
    
    print(new_row["writer"] , results[0]["screen_name"])
    time.sleep(0.5)
    new_row["twitter_name"] = results[0]["screen_name"]   # choose first search result
    dict_writer.writerow(new_row)
