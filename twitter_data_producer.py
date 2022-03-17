import os
import datetime
import json
import pprint

import tweepy

from kafka_producer import producer

bearer_token = os.environ["TWITTER_BEARER_TOKEN"]


class TopicStream(tweepy.StreamingClient):
    def __init__(self, topic, **kwargs):
        self.topic = topic
        super().__init__(**kwargs)

    def on_tweet(self, tweet):
        data = {
            "streamed_at": str(datetime.datetime.now()),
            "id": tweet.id,
            "text": tweet.text,
            "source": tweet.source,
            "lang": tweet.lang,
            "data": tweet.data,
            "entities": tweet.entities,
            "geo": tweet.geo,
            "public_metrics": tweet.public_metrics,
        }
        json_payload = json.dumps(data)
        byte_payload = bytes(json_payload, "utf-8")
        r = producer.send(self.topic, value=byte_payload)
        r.is_done


streaming_client = TopicStream(
    topic="recent_tweets_downloader", bearer_token=bearer_token
)
streaming_client.add_rules(tweepy.StreamRule("solana"))
streaming_client.filter()
