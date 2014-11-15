from twilio.rest import TwilioRestClient
from bs4 import BeautifulSoup
import urllib2

# twilio account validation
account_sid = #twilio account id
auth_token  = #twilio auth token
client = TwilioRestClient(account_sid, auth_token)

# info for making the call + creating the message
reddit_url = "http://www.reddit.com/?limit=1"
my_phone= #my phone number
call_number= #phone number that will be called
my_name = "Aansh Kapadia "

# scrapes the first page of "reddit.com" + returns the top headline
def scrape_reddit(url):
	response = urllib2.urlopen(url)
	soup = BeautifulSoup(response,"lxml")
	# finds span tag where rank = 1 (referring to the top headline)
	for span in soup.findAll('span', "rank"):
	    if span.string == "1":
	    	top_reddit_div = span.parent
	# extracts the text from the top headline
	for link in top_reddit_div.find_all('a', class_="title"):
		reddit_text = link.get_text()
	return reddit_text

# returns the properly formatted twimlet_url to enable twilio's "say" voice command
def convert_to_twimlet(string):
    string = string.replace (" ", "+")
    twimlet_url = "http://twimlets.com/message?Message%5B0%5D=" + string
    return twimlet_url
    
# function calls
message = scrape_reddit(reddit_url)
my_name += message
twimlet = convert_to_twimlet(my_name)
call = client.calls.create(to=call_number, from_=my_phone, url=twimlet)
