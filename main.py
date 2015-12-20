# encoding: utf-8
import webbrowser
import os
from loklak import Loklak

print("Retrieving Tweets...")
query="Star Wars"
l = Loklak()
tweets=l.search(query)

tweet_struct = "<h5>@username</h5>"+"\n"+"<p class='txt'>txt</h4><br>"+"\n"+"<p>"
htmlParsedTweets=""

for tweet in tweets['statuses']:
	htmlTweet = tweet_struct.replace('username', tweet['screen_name']).replace('txt', tweet['text'])
	htmlParsedTweets = htmlParsedTweets+htmlTweet

origin_htmlContent = None
with open('index.html', 'r') as file :
  origin_htmlContent = file.read()

htmlContent = origin_htmlContent.replace('replace', htmlParsedTweets)

with open('results.html', 'w') as file:
  file.write(htmlContent.encode('utf-8'))

webbrowser.open_new_tab('file://'+os.getcwd()+"/results.html")