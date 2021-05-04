from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess
from labirint.bookparser import settings

from labirint.bookparser.spiders.labirint import LabirintSpider

if __name__ == '__main__':
    crawler_setings = Settings()
    crawler_setings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_setings)
    process.crawl(LabirintSpider)
    process.start()
