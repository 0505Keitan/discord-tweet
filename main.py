import discord
from requests_oauthlib import OAuth1Session

CK = "*****"
CS = "*****"
AT = "*****"
AS = "*****"

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.author.id == 0000000000 :
    	if msg.content.startswith('//'):
    	    return
    	url = 'https://api.twitter.com/1.1/statuses/update.json'
    	params = {"status":  msg.content + ' #AppleEvent'}
    	twitter = OAuth1Session(CK, CS, AT, AS)
    	req = twitter.post(url, params = params)
    	if req.status_code == 200:
    		print ("ツイート完了")
    	else:
    		print ("ツイートできませんでした: %d" % req.status_code)   

client.run('********')