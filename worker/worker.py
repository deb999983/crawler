import json
import logging
import os
import signal

import django
import redis
import requests
from django.conf import settings
from django.db import transaction, IntegrityError
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class Worker:

	def __init__(self):
		self.status = 'free'
		self.redis_conn = redis.Redis(charset="utf-8", decode_responses=True, **settings.QUEUE_CONN_PARAMS)
		print(settings.QUEUE_CONN_PARAMS)

		self._kill_now = False
		signal.signal(signal.SIGINT, self.kill)
		signal.signal(signal.SIGTERM, self.kill)

	def kill(self, *args):
		self._kill_now = True

	def run(self):
		from app.models import WebLinkContent

		while not self._kill_now:
			with transaction.atomic():

				message = self.redis_conn.blpop(["crawler_queue"], 30)
				if not message:
					continue

				link = json.loads(message[1])
				url, code = link['url'], link['code']
				self.redis_conn.srem("crawler_codes", code)

				result_str = '\nScrapping Link: {0}'.format(url)
				response = requests.get(url)
				soup = BeautifulSoup(response.content, 'html.parser')

				try:
					link_content, created = WebLinkContent.objects.get_or_create(code=code, defaults=dict(
						title=soup.title.text, url=url, content=response.content
					))
					if created:
						result_str = result_str + '\t\t....Done'
					else:
						result_str = result_str + '\t\t....Already Scrapped'
				except IntegrityError as e:
					print(e)

				print(result_str)


if __name__ == '__main__':

	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
	django.setup(set_prefix=False)

	w = Worker()
	w.run()


