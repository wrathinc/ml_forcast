def redt():
    import praw
    reddit = praw.Reddit(client_id='QNJRuE2-rlLEJA',client_secret='T8ua4m3a7ijr2ziBPiFFzI2gAvI',password='T0236346hd', user_agent='prawTut',username='tipsy3521')
    sdubreddit = reddit.subreddit('python')

    hot_python = sdubreddit.hot(limit=10)

    for submission in hot_python:
        if not submission.stickied:
            print('Title: {}, ups: {}, downs: {}, have we vistied: {},subreddit_id: {}'.format(submission.title,
                                                                            submission.ups,
                                                                            submission.downs,
                                                                            submission.visited,submission.subreddit_id))

    update = reddit.live('t5_2qh0y')



redt()





