Run Services

```
docker-compose up
```

This will start the following services,
```
[+] Running 5/5
 ⠿ Container crawler_queue             Started                                                                                                          0.6s
 ⠿ Container crawler_db             Started                                                                                                          0.7s
 ⠿ Container crawler_worker_monitor    Started                                                                                                          0.6s
 ⠿ Container crawler-crawler_worker-1  Started                                                                                                          1.3s
 ⠿ Container crawler_api               Started                                                                                                          1.1s
```

#### API 
http://localhost:9060/swagger/#/crawl/crawl_create

#### Flower Dashboard
http://localhost:8888/flower/tasks


You can try the api using swagger,
<img width="1477" alt="Screenshot 2023-02-05 at 01 38 03" src="https://user-images.githubusercontent.com/9046803/216795552-bb69d3be-fcf3-4dff-a9a6-4c2ec956f812.png">


and visit flower to see the state of the tasks.
<img width="1728" alt="Screenshot 2023-02-05 at 01 37 31" src="https://user-images.githubusercontent.com/9046803/216795539-beb4bbe5-4f3d-45da-a196-fadad417409e.png">
