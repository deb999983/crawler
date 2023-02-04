import hashlib
import json

import redis
from django.conf import settings


redis_conn = redis.Redis(charset="utf-8", decode_responses=True, **settings.QUEUE_CONN_PARAMS)


def create_hash(url):
	salted_url = url + settings.SECRET_KEY
	code = hashlib.sha256(salted_url.encode()).hexdigest()
	return code


def enqueue(url):
	code = create_hash(url)
	if redis_conn.sismember('crawler_codes', code):
		return url, code

	redis_conn.rpush("crawler_queue", json.dumps({"url": url, "code": code}))
	redis_conn.sadd("crawler_codes", code)
	return url, code
