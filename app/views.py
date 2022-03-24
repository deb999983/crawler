from django.http import Http404
from rest_framework.exceptions import NotFound
from rest_framework.generics import CreateAPIView, RetrieveAPIView

import utils
from app.models import WebLinkContent
from app.serializers import LinkContentSerializer, LinkQueueSerializer


class ScheduleCrawlView(CreateAPIView):
	serializer_class = LinkQueueSerializer
	queryset = WebLinkContent.objects.all()

	def perform_create(self, serializer):
		url = serializer.validated_data['url']

		url, code = utils.enqueue(url)
		serializer.validated_data["code"] = code
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

