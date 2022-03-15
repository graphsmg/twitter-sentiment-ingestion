# twitter-sentiment-ingestion
{twitter -> kafka -> spark -> mongo -> plotly} ingestion pipelines

## setting up dev environment

0. recommended you create a virtual environment

```
 conda create -n reddit python=3.7
 conda activate reddit 
 python -m pip install -r requirements.txt
```

1. install (1) docker and (2) docker compose. 

2. start up docker services
```
docker-compose up -d
```
3. install kafka tools 

check for latests download https://kafka.apache.org/quickstart and then unzip and cd into directory
```
tar -xzf kafka_2.13-3.1.0.tgz
cd kafka_2.13-3.1.0
```



## helpful dev commands 

```
~/Downloads/kafka_2.13-3.1.0/bin/kafka-console-consumer.sh --topic test_topic --from-beginning --bootstrap-server localhost:29092
```

