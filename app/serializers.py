import hashlib

from django.conf import settings
from rest_framework import serializers
from app.models import WebLinkContent


class LinkQueueSerializer(serializers.Serializer):
	code = serializers.CharField(read_only=True)
	url = serializers.URLField()

	def validate(self, attrs):
		salted_url = attrs['url'] + settings.SECRET_KEY
		attrs['code'] = hashlib.sha256(salted_url.encode()).hexdigest()
		return attrs


class LinkContentSerializer(serializers.ModelSerializer):
	class Meta:
		model = WebLinkContent
		fields = '__all__'
