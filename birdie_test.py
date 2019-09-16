"""
                    Insight Data Engineering SEA'19C
Project: Traffic Control of API source
Birdie implementation

"""
from private_twitter_authentication_config import my_system_designer_cred
from birdy.twitter import UserClient
from birdy.twitter import StreamClient
import pprint

CONSUMER_KEY = my_system_designer_cred.consumer_api_key
CONSUMER_SECRET = my_system_designer_cred.consumer_secret_api_key
ACCESS_KEY = my_system_designer_cred.access_token
ACCESS_SECRET = my_system_designer_cred.access_token_secret
client = UserClient(CONSUMER_KEY,
                    CONSUMER_SECRET,
                    ACCESS_KEY,
                    ACCESS_SECRET)
response = client.api.users.show.get(screen_name='twitter')
pprint.pprint(response.data)

# # DO SOME STREAMING
# client = StreamClient(CONSUMER_KEY,
#                     CONSUMER_SECRET,
#                     ACCESS_KEY,
#                     ACCESS_SECRET)
# resource = client.stream.statuses.filter.post()
