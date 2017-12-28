import requests
import random
import twitter

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
	number_items_to_return = 3
	try:
		request_response = requests.get("https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=" + str(number_items_to_return) + "&format=json")
		response_json = request_response.json()
	except Exception:
		print("Could not get Wiki pages!")
		return 1

	titles = []
	for response_item in response_json['query']['random']:
		titles.append(response_item['title'])
	join_words = ["discovered", "created", "caused", "killed", "invented", "drowned", "found", "founded"]
	output = titles[0] + " and " + titles[1] + " " + join_words[random.randint(0, len(join_words) - 1)] + " " + titles[2]
	tweet(output)
	return 0

if __name__ == "__main__":
	main()
	exit()
