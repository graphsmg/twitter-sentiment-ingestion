import os
import datetime
import uuid
import json

import requests


def create_headers():
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def create_url(keyword="solana", max_results=50):
    # searches recent tweets
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    # change params based on the endpoint you are using
    query_params = {
        "query": keyword,
        # 'start_time': start_date,
        # 'end_time': end_date,
        "max_results": max_results,
        "expansions": "author_id,in_reply_to_user_id,geo.place_id",
        "tweet.fields": "id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source",
        "user.fields": "id,name,username,created_at,description,public_metrics,verified",
        "place.fields": "full_name,id,country,country_code,geo,name,place_type",
        "next_token": {},
    }
    return (search_url, query_params)


def connect_to_endpoint(url, headers, params, next_token=None):
    params["next_token"] = next_token  # params object received from create_url function
    response = requests.request("GET", url, headers=headers, params=params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


# write tweets to producer
url, query_params = create_url()
headers = create_headers()
data = connect_to_endpoint(url, headers, query_params)
batch_uuid = str(uuid.uuid4())
batch_timestamp = datetime.datetime.now().isoformat()
for tweet in data.get("data"):
    payload = {
        "batch_uuid": batch_uuid,
        "batch_timestamp": batch_timestamp,
        "request_uuid": str(uuid.uuid4()),
        "request_timestamp": datetime.datetime.now().isoformat(),
        "twitter_api_data": tweet,
    }

    json_payload = json.dumps(payload)
    byte_payload = bytes(json_payload, "utf-8")
    r = producer.send(topic="recent_tweets_downloader", value=byte_payload)
    r.is_done
