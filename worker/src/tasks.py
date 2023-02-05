from bs4 import BeautifulSoup
from django.db import IntegrityError
import requests
from config.celery_conn import app
from applications.crawler.models import WebLinkContent


@app.task(name="worker.crawl_url")
def crawl_url(url, code):
    result_str = '\nLink: {0}'.format(url)
    try:
        response = requests.get(url, timeout=2)
        soup = BeautifulSoup(response.content, 'html.parser')

        link_content, created = WebLinkContent.objects.get_or_create(code=code, defaults=dict(
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
    return result_str