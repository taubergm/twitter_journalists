import oauth, tweepy
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



#-----------------------------------------------------------------------
# perform a user search 
# twitter API docs: https://dev.twitter.com/rest/reference/get/users/search
#-----------------------------------------------------------------------

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_key, config.access_secret)
api=tweepy.API(auth)


infile = "writers_twitter.csv"
writer_data = open(infile)
csv_reader = csv.reader(writer_data)


OUTFILE = "writers_plus_twitter_follows.csv"
output_file = open(OUTFILE, 'w')

keys = ['writer', 'twitter_name', 'num_followers', 'num_articles', 'gender', 'last_url']
dict_writer = csv.DictWriter(output_file, keys)
dict_writer.writeheader()
for row in csv_reader:
    new_row = {}
    new_row["writer"] = row[0]
    new_row["twitter_name"] = row[1]
    new_row["num_articles"] = row[2]
    new_row["gender"] = row[3]
    new_row["last_url"] = row[4]

    print(new_row["twitter_name"])
    try:
        user = api.get_user(new_row["twitter_name"])
    except:
        print("missed user %s" % new_row["twitter_name"])
        continue
    
    new_row["num_followers"] = user.followers_count
    
    print (user.screen_name, user.followers_count)
    time.sleep(3)
    dict_writer.writerow(new_row)
