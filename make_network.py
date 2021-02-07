import csv
import time
import sys
import re
import subprocess
import networkx as nx
import matplotlib.pyplot as plt

csv.field_size_limit(sys.maxsize)



infile = "writers_plus_twitter_network_final.csv"
writer_data = open(infile)
csv_reader = csv.reader(writer_data)
writers = set()
for row in csv_reader:
    twitter_name = row[1]
    num_followers = row[2]

    if (row[0] == "writer"):
        continue

    if (int(num_followers) < 300):
        continue

    writers.add(twitter_name)

G = nx.Graph()


infile = "writers_plus_twitter_network_final.csv"
writer_data = open(infile)
csv_reader = csv.reader(writer_data)
for row in csv_reader:
    writer = row[0]
    twitter_name = row[1]
    num_followers = row[2]
    num_articles = row[3]
    gender = row[4]
    last_url = row[5]
    following = row[6].split(':')
    num_following = len(following)
    
    if (writer == "writer"):
        continue

    #print writer, twitter_name, num_followers, num_articles

    if (int(num_followers) < 300):
        continue
    
    for user in following:
        if (user in writers):
            #print "%s - %s - %s - %s" % (writer, num_following, twitter_name, user)
            G.add_edge(twitter_name, user)


writer_degrees =  dict(G.degree)
fieldnames = ['writer', 'degrees']
#print writer_degrees

with open('mycsvfile.csv', 'wb') as f:  
    w = csv.DictWriter(f, writer_degrees.keys())
    w.writeheader()
    w.writerow(writer_degrees)

for key, value in writer_degrees.items():
    print key + ',' + str(value)

#deg_cen = nx.degree_centrality(G)
#print deg_cen


#nx.draw_networkx_nodes(G = graph, pos = pos, node_list = graph.nodes(), node_color = 'r', alpha = 0.8, node_size = [counts['edges'][s]*for s in G.nodes()])
#plt.savefig("./map_0.png", format = "png", dpi = 300)
#plt.show()



#betweeness_centrality = nx.betweenness_centrality(G)
#fieldnames = ['writer', 'betweeness_centrality']
#with open('betweeness_centrality.csv', 'wb') as f:  
#    w = csv.DictWriter(f, betweeness_centrality.keys())
#    w.writeheader()
#    w.writerow(betweeness_centrality)


#eigenvector_centrality = nx.eigenvector_centrality(G)
#fieldnames = ['writer', 'eigenvector_centrality']
#with open('eigenvector_centrality.csv', 'wb') as f:  
#    w = csv.DictWriter(f, eigenvector_centrality.keys())
#    w.writeheader()
#    w.writerow(eigenvector_centrality)

#closeness_centrality = nx.closeness_centrality(G)
#fieldnames = ['writer', 'closeness_centrality']
#with open('eigenvector_centrality.csv', 'wb') as f:  
#    w = csv.DictWriter(f, closeness_centrality.keys())
#    w.writeheader()
#    w.writerow(closeness_centrality)


