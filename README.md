tumblrfollows
=============

Basic python script to list following and followed blogs on Tumblr

Currently accepts no arguments and contains debug code. Outputs one username per line.


Clone to anywhere you like, create a file named .tumblr in your home directory
.tumblr is a yaml file and should contain the following:

    consumer_key: your_api_consumer_key
    consumer_secret: your_api_secret
    oauth_token: your_oauth_token
    oauth_token_secret: your_oauth_secret
    blog_url: your_url

blog_url is just the bit BEFORE tumblr.com
  e.g. fluffypuppies.tumblr.com would put "blog_url: fluffypuppies" 

To get the api keys and oauth tokens:
Create an app: https://www.tumblr.com/oauth/apps

Fetch your tokens: https://api.tumblr.com/console/calls/user/info

Only tested on Linux, currently unable to test on Windows or Mac	

Dependancies:
oauth
PyYAML
pytumblr
