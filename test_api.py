import threading
import time

import requests
from bs4 import BeautifulSoup


def run():
	response = requests.get("https://en.wikipedia.org/wiki/Data_management")
	soup = BeautifulSoup(response.content, 'html.parser')

	rel_links = soup.select('a[href^="/wiki/"]')
	links = map(lambda rel_link: "https://en.wikipedia.org" + rel_link.attrs["href"], rel_links)

	for link in links:
		time.sleep(0.1)
		t = threading.Thread(target=lambda: requests.post("http://127.0.0.1:9060/crawl/", json={"url": link}))
		t.start()


if __name__ == "__main__":
	run()
