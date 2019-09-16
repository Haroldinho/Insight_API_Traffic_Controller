"""
                    Insight Data Engineering SEA'19C
Project: Traffic Control of API source


"""

from private_twitter_authentication_config import SystemDesignerCredentials
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import logging


# all debug will be recorded
# other information logging.INFO, logging.WARNING, logging.CRITICAL
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename="twitter_connector.log", filemode="w", format="%(asctime)s: %(process)d - %(levelname)s - %(message)s")

logging.debug("Logging into Twitter API")
# General Authentication
config_instance = SystemDesignerCredentials()
consumer_key = config_instance.consumer_api_key
consumer_secret = config_instance.consumer_secret_api_key
access_token = config_instance.access_token
access_secret = config_instance.access_token_secret


# Basic listener printing received tweets to stdout
class MySimpleStreamListener(StreamListener):
    def on_connect(self):
        logging.info("Successfully connected")
        pass

    def on_status(self, status):
        logging.info("Current Status" + status)
        return

    def on_data(self, data):
        logging.info(data)
        return True

    def on_error(self, status):
        logging.error(status)


if __name__ == '__main__':
    # This handles Twitter authentication and the
    # connection to Twitter Streaming API
    my_stream_listener = MySimpleStreamListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    my_stream = Stream(auth, listener=my_stream_listener)

    # Filter Twitter Streams to capture data by keywords:
    my_stream.filter(track=['gelato', 'pizza', 'pie', 'ice-cream', 'coca', 'coca-cola', 'coke'])


