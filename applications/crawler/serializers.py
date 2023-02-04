from rest_framework import serializers
from applications.crawler.models import WebLinkContent


class LinkQueueSerializer(serializers.Serializer):
	code = serializers.CharField(read_only=True)
	url = serializers.URLField()


class LinkContentSerializer(serializers.ModelSerializer):
	class Meta:
		model = WebLinkContent
		fields = '__all__'
