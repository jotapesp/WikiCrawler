# WikiCrawler

WikiCrawler is a small application written in Python with the solely purpose of printing to screen the page title of the entered Wikipedia URL and also the titles of all the internal links present on the original page. The program initially works only for PT-BR Wikipedia pages and I intend to add other Web Scraping functions other than just extracting the title text in the future.

## How to use

You can simply run  
  `python wiki_crawler.py`  
But if you prefer, you can inform the URL in the command line as well and the program will skip prompting you for the URL while running  
  `python wiki_crawler.py [url]`  
The same can be applied if you want to inform beforehand if the application should crawl through the pages with languages different than the original page, that is, pages that are not in Portuguese. Use `foreign` for allowing different languages or `not_foreign` if you want only PT-BR pages. Entering an argument different from those two will make the program choose for the default PT-BR pages only.   
  `python wiki_crawler.py [url] [foreign/not_foreign]`  
