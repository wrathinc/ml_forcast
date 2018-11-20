from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import MySQLdb
import time

conn = MySQLdb.connect("localhost","root", "root", "dbname")
c = conn.cursor()


with open('twitter-files/credentials.txt',"r") as input_file:
		lists = []
		readfile = input_file.read()
		scefile = readfile.split('\n')[0].split('app_key=')[1]
		apfile = readfile.split('\n')[1].split('app_secret=')[1]
		oaut = readfile.split('\n')[2].split('oauth_token=')[1]
		oaut_secret = readfile.split('\n')[3].split('oauth_token_secret=')[1]
	
ckey = scefile
csecret = apfile
atoken = oaut
asecret = oaut_secret
username = 'Python'


class listener(StreamListener):
	def on_data(self, data):
		try:
			if data.split(',"created_at":"')[1]:
				tweet = data.split(',"text":"')[1].split(',"source')[0]
				print "Inserting tweets into tabele %s", tweet  
				time.sleep(2)
				#username = data.split(',"text"')[1].split('","screen_name')[0]
			c.execute("INSERT  INTO twit (time,username,tweet) VALUES (%s,%s,%s)",
			(time.time(),username, tweet))
			conn.commit()
			return True

		except BaseException, e:
			print 'failed ondata, ', str(e)
			time.sleep(5)

	def on_error(self, status):
		print status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Trump"])



