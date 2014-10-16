#!/usr/bin/python
import pytumblr
import yaml
import os
import urlparse
import code
import oauth2 as oauth

yaml_path = os.path.expanduser('~') + '/.tumblr'

if not os.path.exists(yaml_path):
    tokens = new_oauth(yaml_path)
else:
    yaml_file = open(yaml_path, "r")
    tokens = yaml.safe_load(yaml_file)
    yaml_file.close()

client = pytumblr.TumblrRestClient(
    tokens['consumer_key'],
    tokens['consumer_secret'],
    tokens['oauth_token'],
    tokens['oauth_token_secret']
)

# Make the request
followers = client.following(limit=1, offset=0)
print followers['total_blogs']
#print followers['users'][0]['name']
#print followers['users']
j = followers['total_blogs']
i = 0
followersdiv = j // 20
followersmod = (j % 20)

#print followersdiv
#print followersmod
timetodie = 0
i = 0
z = 0
while 1 :
    followersoffset = i * 20
    #print "Followers offset: {}".format(followersoffset)
    if i < followersdiv:
        rangelimit = 20
    else:
        rangelimit = (followersmod)

    #print "Rangelimit: {}".format(rangelimit)
    followers = client.following(limit=rangelimit, offset=followersoffset)
    for x in range(0, rangelimit):
        z += 1
        #print "Group: {}".format(i)
        #print "Follower: {}".format(x)
        try:
            print followers['blogs'][x]['name']
        except:
            break
    i += 1
    if i == (followersdiv+1):
        if z != followers['total_blogs']:
            print ""
            print "There's a bug somewhere, pester James"
            print ""
        print "Reported: {}".format(j)
        print "Counted : {}".format(z)
        break

