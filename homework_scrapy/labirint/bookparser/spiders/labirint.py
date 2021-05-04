import scrapy
from scrapy.http import HtmlResponse
from labirint.bookparser.items import BookparserItem


class LabirintSpider(scrapy.Spider):
    name = 'labirint'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/search/философия/']

    def parse(self, response:HtmlResponse):

        links = response.xpath('//div[contains(@class, "products-row")]'
                               '/div//a[contains(@class, "title-link")]/@href').getall()
        for short_link in links:
            link = f"https://{LabirintSpider.allowed_domains[0]}{short_link}"
            yield response.follow(link, callback=self.process_item)

        next_page = response.xpath('//div[contains(@class, "pagination-next")]'
                                   '/a[contains(@class, "pagination-next")]/@href').get()
        full_link_next_page = f"{LabirintSpider.start_urls[0]}{next_page}"


        if next_page:
            yield response.follow(full_link_next_page, callback=self.parse)

    def process_item(self,response:HtmlResponse):
        item = BookparserItem()

        item['url'] = response.url
        item['header'] = response.xpath('//h1/text()').get()
        item['author'] = response.xpath('//a[contains(@data-event-label, "author")]/text()').get()
        item['price'] = response.xpath('//div[contains(@class, "priceold")]/span/text()').get()
        item['rating'] = response.xpath('//div[contains(@id,"rate")]/text()').get()
        print()
        yield item



