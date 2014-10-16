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
followers = client.followers('lazytechsupport.tumblr.com', limit=1, offset=0)
print followers['total_users']
#print followers['users'][0]['name']
#print followers['users']
total_followers = followers['total_users']
followersdiv = total_followers // 20
followersmod = total_followers % 20

#print followersdiv
#print followersmod
#print ""
current_offsetgroup = 0
counted_followers = 0
countdown_followers = total_followers
while 1 :
    followersoffset = current_offsetgroup * 20
#    print "Followers offset: {}".format(followersoffset)
    if current_offsetgroup < followersdiv:
        rangelimit = 20
    else:
        rangelimit = followersmod

#    print "Rangelimit: {}".format(rangelimit)
#    followers = client.followers('lazytechsupport.tumblr.com', limit=rangelimit, offset=followersoffset)
    followers = client.followers(tokens['blog_url']+'.tumblr.com', limit=rangelimit, offset=followersoffset)
    for x in range(0, rangelimit):
        counted_followers += 1

#        print "Group: {}".format(current_offsetgroup)
#        print "Follower: {}".format(x)
        try:
            print followers['users'][x]['name']
        except:
            break
#        countdown_followers -= 1
#        print countdown_followers

    current_offsetgroup += 1
    if current_offsetgroup == (followersdiv+1):
        if counted_followers != followers['total_users']:
            print ""
            print "There's a bug somewhere, pester James"
            print ""
        print "Reported : {}".format(total_followers)
        print "Counted  : {}".format(counted_followers)
        break

