import scrapy
from scrapy.http import HtmlResponse
from labirint.bookparser.items import BookparserItem


class Book24Spider(scrapy.Spider):
    name = 'book24'
    allowed_domains = ['book24.ru']
    start_urls = ['https://book24.ru/search/?q=философия']

    def parse(self, response: HtmlResponse):

        links = response.xpath('//a[contains(@itemprop, "name")]/@href').getall()

        for short_link in links:
            link = f"https://{Book24Spider.allowed_domains[0]}{short_link}"
            yield response.follow(link, callback=self.process_item)

        page = 1
        while page <= 10:
            next_page_link = f"https://book24.ru/search/page-{page}?q=философия"
            yield response.follow(next_page_link, callback=self.parse)
            page += 1

    def process_item(self, response: HtmlResponse):
        item = BookparserItem()

        item['url'] = response.url
        item['header'] = response.xpath('//h1/text()').get()
        item['author'] = response.xpath('//a[contains(@itemprop, "author")]//text()').get()
        item['price'] = response.xpath('//b[contains(@itemprop, "price")]//text()').get()
        item['rating'] = response.xpath('//div[contains(@class, "rating__rate-value")]//text()').get()
        print()
        yield item
