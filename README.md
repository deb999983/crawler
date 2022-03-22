Implemented a very basic crawler service. The crawler service is composed of 4 components

#### Components
- **ResultDatabase**: This is a mysql database that stores the crawled url results.
- **CrawlerQueue**: This is a queue that will hold the list of urls to be crawled.
- **CrawlerServer**: This service is responsible for taking the url requests for crawling. This service
just queues up the url for crawling in the **CrawlerQueue**, that will be picked by any running **CrawlerWorker**
  for scraping.
- **CrawlerWorker**: This component is responsible for crawling. It picks up urls from the queue and crawls them
and then stores the results in the **ResultDatabase**.
  

#### Build
To build the service and workers run command
 - ```docker-compose up --scale crawler_worker=5```

This command will do the following
 - Start the **result_db**
 - Start up the **crawler_queue**
 - Start up the **crawler_server**
 - Start up 5 instances of **crawler_worker**

The crawler service api is hosted at port **9060**, so if you browse to,
**http://localhost:9060/swagger/** you can see 2 apis hosted for the service.

 - /crawl/: This api will register the request for crawling a website and will return an identifier which can be
user to fetch the contents later.
 - /crawl/content/{code}/: **code** is the identifier returned when the website was registered for scraping. User can 
   use this code to fetch the scraping results.
   

#### Testing
To test the service I have written a simple script that crawls a particular wiki page.

Run the command
- ```python test_api.py```,
after starting up all the services, you can then see the results getting populated in the
database.
  
Or you can anyways play with the apis.
