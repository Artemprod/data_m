# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, Compose, TakeFirst


def get_photo_big(url):
    url = url.replace('/f_auto,q_90,w_40,h_40,c_pad,b_white,d_photoiscoming/', '/')
    url = url.replace('w_40,h_40', 'w_2000,h_2000')
    return url


#
# def del_gap(params_2):
#     params_2 = params_2.remove('')
#     return params_2


class LerroymerlinItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(get_photo_big))
    params_1 = scrapy.Field()
    params_2 = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    pass
