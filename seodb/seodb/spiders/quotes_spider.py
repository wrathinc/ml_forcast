import scrapy
import csv

class QuotesSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        'https://adkinsheatandair.com/',
    ]
    print(f"cralwling: {start_urls}")

    def parse(self, response):
        for start_urls in response.css('body'):
            yield {
                'text': start_urls.css('#_the_copyright > div > ul > li:nth-child(1)').extract_first(),
                'phonenumber': start_urls.css('#_the_map_wrapper > div > div > div > ul > li > p > br:').extract_first(),
                #'tags': quote.css('div.tags a.tag::text').extract(),
            }
       


