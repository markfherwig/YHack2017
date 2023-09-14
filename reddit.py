import praw
reddit = praw.Reddit(username="shryans", password="Shryans@27", client_id="clbYCsRuqIqVwA", client_secret="cSIK9IunrBE_4PPMRJmK1-qrp1k", user_agent="usragent")

sub = reddit.subreddit('Bitcoin')
top100 = sub.top(limit=100)
for post in top100:
	print(vars(post))

