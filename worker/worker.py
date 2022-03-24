import json
import logging
import os
import signal
import time

import django
import redis
import requests
from django.conf import settings
from django.db import transaction, IntegrityError
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class Worker:

	def __init__(self):
		self.scrapped_links = []
		self.redis_conn = redis.Redis(charset="utf-8", decode_responses=True, **settings.QUEUE_CONN_PARAMS)
		print(settings.QUEUE_CONN_PARAMS)

		self._kill_now = False
		signal.signal(signal.SIGINT, self.kill)
		signal.signal(signal.SIGTERM, self.kill)

		self.queue_empty_message = "Url Queue is Empty....."
		self.queue_empty_message_printed = False

	def kill(self, *args):
		self._kill_now = True
		print(*self.scrapped_links, len(self.scrapped_links), sep="\n")

	def crawl_url(self, url, code):
		self.scrapped_links.append(url)
		result_str = '\nLink: {0}'.format(url)
		try:
			response = requests.get(url, timeout=2)
			soup = BeautifulSoup(response.content, 'html.parser')

			link_content, created = self.WebLinkContentModel.objects.get_or_create(code=code, defaults=dict(
				title=soup.title.text if soup.title else '',
				url=url, content=response.content, status_code=response.status_code,
			))
			if created:
				result_str = result_str + '\t\t....Done'
			else:
				result_str = result_str + '\t\t....Already Scrapped'
		except IntegrityError as e:
			result_str = result_str + '\n{0}'.format(e)
		except Exception as e:
			result_str = result_str + '\n{0}'.format(e)

		print(result_str)

	def run(self):
		from app.models import WebLinkContent
		self.WebLinkContentModel = WebLinkContent

		while not self._kill_now:
			with transaction.atomic():
				message = self.redis_conn.lpop("crawler_queue")
				if not message:
					if not self.queue_empty_message_printed:
						print("\n{0}\n".format(self.queue_empty_message))
						self.queue_empty_message_printed = True
					time.sleep(0.5)
					continue

				self.queue_empty_message_printed = False
				link = json.loads(message)
				url, code = link['url'], link['code']
				self.redis_conn.srem("crawler_codes", code)

				self.crawl_url(url, code)


if __name__ == '__main__':

	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
	django.setup(set_prefix=False)

	w = Worker()
	w.run()


