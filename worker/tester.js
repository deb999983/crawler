function seedUrls() {
    urls = []
    for (i = 1; i <= 10; i++) {
        urls.push(`http://a${i}.com`)
    }

    urls.forEach(function(url) {
        fetch(
            "http://localhost:9060/crawl/", {
                "method": "POST",
                "headers": {"Content-Type": "application/json"},
                "body": JSON.stringify({"url": url})
            }
        );
    });
}



