import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from leroy_merlin.lerroymerlin.items import LerroymerlinItem


class LeroymerlinSpider(scrapy.Spider):
    name = 'leroymerlin'
    allowed_domains = ['leroymerlin.ru']
    # start_urls = ['https://leroymerlin.ru/search/?q=обои']

    def __init__(self, search):
        super().__init__()
        url = f"https://leroymerlin.ru/search/?q={search}"
        self.start_urls = [url]

    def parse(self, response: HtmlResponse):

        links = response.xpath('//div[@data-qa-product]/a/@href').getall()
        print()
        for link in links:
            print()
            yield response.follow(link, callback=self.parse_item)
            print()

        next_page = response.xpath('//a[contains(@data-qa-pagination-item,"right")]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)




    def parse_item(self, response: HtmlResponse):
        # item = LerroymerlinItem()
        # item['name'] = response.xpath('//h1/text()').get()

        loader = ItemLoader(item=LerroymerlinItem(), response=response)
        loader.add_xpath('name', '//h1/text()')
        loader.add_xpath('photos', '//uc-variant-card//@src')
        loader.add_xpath('params_1', '//dl[contains(@class, "def-list")]/div[contains(@class,"def-list__group")]/dt//text()')
        loader.add_xpath('params_2', '//dl[contains(@class, "def-list")]/div[contains(@class,"def-list__group")]/dd/text()')
        print()
        yield loader.load_item()

