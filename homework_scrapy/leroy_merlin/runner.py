import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from leroy_merlin.lerroymerlin import settings
from leroy_merlin.lerroymerlin.spiders.leroymerlin import LeroymerlinSpider
from urllib.parse import quote_plus

if __name__ == '__main__':
    search = str(input('что ищем ?: '))
    # search = 'обои'
    crawler_setings = Settings()
    crawler_setings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_setings)
    process.crawl(LeroymerlinSpider, search=search)
    process.start()
