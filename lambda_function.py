import logging
import redis
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


redis_client = redis.Redis(host='electric-cache.g1pva1.ng.0001.aps1.cache.amazonaws.com',
                           port=6379)

if redis_client.ping():
    logging.info("Connected to Redis")


def cache_it(data_to_cache):
    try:
        for data in data_to_cache:
            k, v = list(data.items())[0]
            redis_client.set(k, v)
    except KeyError:
        logging.exception(f"Not able to cache the data {data_to_cache}")
        return False
    else:
        return True


def get_it(key_to_get):
    value_to_return = None
    try:
        value_to_return = redis_client.get(key_to_get)
    except Exception:
        raise
    else:
        redis_client.delete([key_to_get])
    return value_to_return


def flush_all_cache():
    return redis_client.flushall()


def lambda_handler(event, context):
    logging.info(f"here is the event {event}")
    try:
        if event["cache"]:
            data_to_cache: [{}] = event["data_to_cache"]
            return cache_it(data_to_cache)
    except KeyError:
        pass

    try:
        if event["get"]:
            return get_it(event["key_to_get"])
    except KeyError:
        pass

    try:
        if event["flush"]:
            return flush_all_cache()
    except KeyError:
        pass




