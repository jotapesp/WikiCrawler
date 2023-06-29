# WikiCrawler

WikiCrawler is a small application written in Python with the solely purpose of printing to screen the page title of the entered Wikipedia URL and also all the titles of all the internal links present on the original page.

## How to use

You can simply run
    `python wiki_crawler.py`
But if you prefer, you can inform the URL in the command line as well and the program will skip asking for your input while running
    `python wiki_crawler.py [url]`
The same can be applied if you want to inform beforehand if the application should scrape URLs of pages with languages different than the original page, that is, pages that are not in Portuguese.
    `python wiki_crawler.py [url] [foreign/not_foreign]`
