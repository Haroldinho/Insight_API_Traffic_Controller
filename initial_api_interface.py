import logging
import unittest
from requests_oauthlib import OAuth1Session
import json
# pretty print for json files
import pprint
from private_twitter_authentication_config import SystemDesignerCredentials

# all debug will be recorded
# other information logging.INFO, logging.WARNING, logging.CRITICAL
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(filename="twitter_connector.log", filemode="w", format="%(asctime)s: %(process)d - %(levelname)s - %(message)s")

logging.debug("Logging into Twitter API")
# General Authentication
config_instance = SystemDesignerCredentials()
consumer_key = config_instance.consumer_api_key
consumer_secret = config_instance.access_token_secret
# NO CALLBACK URI

# 1) Connection request and fetch request token
request_token_url = "https://api.twitter.com/oauth/request_token"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
fetch_response = oauth.fetch_request_token(request_token_url)

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
logging.info("Got OAuth token:{}".format(resource_owner_key))

# 2) Get authorization by following authorization link
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
logging.info("Please go here and authorize: {}".format(authorization_url))
verifier = input("Paste the PIN here: ")

# 3) Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(consumer_key,
                      client_secret=consumer_secret,
                      resource_owner_key=resource_owner_key,
                      resource_owner_secret=resource_owner_secret,
                      verifier=verifier)
oauth_tokens = oauth.fetch_access_token(access_token_url)


access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]


# Make the request
oauth = OAuth1Session(consumer_key,
                      client_secret=consumer_secret,
                      resource_owner_key=access_token,
                      resource_owner_secret=access_token_secret)

# Add the Tweet ID for the Tweet you are looking for
# You can add up to 50 comma separated IDs
params = {"ids": "apache"}
response = oauth.get("https://api.twitter.com/labs/1/tweets/metrics/private",
                     params=params)
if response.status_code == 404:
    logging.critical("Wrong link to API")
elif response.status_code == 401:
    logging.critical("Wrong credentials")
elif response.status_code == 403:
    logging.critical("Forbidden resource")
elif response.status_code == 503:
    logging.critical("Server not ready to handle the request")

# Pretty print the response
pprint.pprint(json.loads(response.text))



