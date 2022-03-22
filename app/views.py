import json

import redis
from django.conf import settings
from django.http import Http404
from rest_framework.exceptions import NotFound
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from app.models import WebLinkContent
from app.serializers import LinkContentSerializer, LinkQueueSerializer


redis_conn = redis.Redis(charset="utf-8", decode_responses=True, **settings.QUEUE_CONN_PARAMS)


class ScheduleCrawlView(CreateAPIView):
	serializer_class = LinkQueueSerializer
	queryset = WebLinkContent.objects.all()

	def perform_create(self, serializer):
		code = serializer.validated_data['code']
		# if redis_conn.sismember('crawler_codes', code):
		# 	return serializer.validated_data

		redis_conn.rpush("crawler_queue", json.dumps(serializer.validated_data))
		redis_conn.sadd("crawler_codes", serializer.validated_data['code'])
		return serializer.validated_data


class CrawlContentView(RetrieveAPIView):
	serializer_class = LinkContentSerializer
	queryset = WebLinkContent.objects.all()
	lookup_field = 'code'
	lookup_url_kwarg = 'code'

	def retrieve(self, request, *args, **kwargs):
		try:
			return super().retrieve(request, *args, **kwargs)
		except Http404 as e:
			raise NotFound("Either the processing has not begun on the url, or you have the wrong code.")

