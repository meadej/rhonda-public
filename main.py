import requests
import random
import twitter
from datetime import datetime

def tweet(tweet_string):
	api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')
	try:
		api.PostUpdate(tweet_string)
	except Exception:
		print("Could not post update!")
		return 1
	return 0	

def main():
	number_items_to_return = 4
	try:
		request_response = requests.get("https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=" + str(number_items_to_return) + "&format=json")
		response_json = request_response.json()
	except Exception:
		print("Could not get Wiki pages!")
		return 1

	titles = []
	for response_item in response_json['query']['random']:
		titles.append(response_item['title'])
	
	verbs = []
	adverbs = []

	fhandle = open("verbs.txt", 'r')	
	for line in fhandle.readlines():
		verbs.append(line)

	fhandle.close()
	fhandle = open("adverbs.txt", 'r')
	for line in fhandle.readlines():
		adverbs.append(line)

	output = "On this day in " + str(random.randint(1800, int(datetime.now().year))) + ": " + titles[1] + " " + adverbs[random.randint(0, len(adverbs) - 1)].strip() + " " + verbs[random.randint(0, len(verbs) - 1)].strip() + " " + titles[2] + " #" + str(titles[3]).replace(" ", "").replace(",","").replace("(","").replace(")","").replace("-","").replace("'", "").replace('"','')
	tweet(output)
	return 0

if __name__ == "__main__":
	main()
	exit()
