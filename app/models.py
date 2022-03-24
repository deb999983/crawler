from django.db import models


class WebLinkContent(models.Model):
	code = models.CharField(max_length=256, unique=True)
	url = models.URLField(unique=True)
	title = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	status_code = models.PositiveIntegerField()
