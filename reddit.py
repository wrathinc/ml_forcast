import praw 

reddit = praw.Reddit(client_id='clientid', client_secret='secret', password='T0236346hd', useragent='PrawTut', username='u/tipsy3521')
subreddit = reddit.subreddit('python')