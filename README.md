Run Services

```
docker-compose up
```

This will start the following services,
```
[+] Running 5/5
 ⠿ Container crawler_queue             Started                                                                                                          0.6s
 ⠿ Container web_server_db             Started                                                                                                          0.7s
 ⠿ Container crawler_worker_monitor    Started                                                                                                          0.6s
 ⠿ Container crawler-crawler_worker-1  Started                                                                                                          1.3s
 ⠿ Container crawler_api               Started                                                                                                          1.1s
```

#### API 
`http://localhost:9060/swagger/#/crawl/crawl_create`

#### Flower Dashboard
http://localhost:8888/flower/tasks


You can try the api using swagger and visit flower to see the state of the tasks.
