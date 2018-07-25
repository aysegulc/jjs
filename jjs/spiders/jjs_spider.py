# -*- coding: utf-8 -*-
import scrapy
from jjs.items import JjsItem


class JjsSpiderSpider(scrapy.Spider):
    name = "jjs"
    allowed_domains = ["jiujitsutimes.com"]
    start_urls = ['https://www.jiujitsutimes.com/maps/schools/allschools/popular?p=1']

    def parse(self, response):

        for href in response.xpath('//div[contains(@class, "title location")]/a/@href').extract():
            yield scrapy.Request('https://www.jiujitsutimes.com/maps/' + href,
                                 self.parse_school)

        next_page = response.xpath('//a[@rel="next"]/@href').extract_first()
        if next_page is not None:
            # next_page = response.urljoin(next_page)
            yield scrapy.Request('https://www.jiujitsutimes.com/maps/' + next_page,
                                 callback=self.parse)

    def parse_school(self, response):
        business = JjsItem()

        business['Name'] = response.xpath('//div[contains(@itemtype,"Organization")]/'
                                          'span[@itemprop="name"]/text()').extract_first(default='').strip()

        business['Website'] = response.xpath('//div[contains(@itemtype,"Product")]/'
                                             'span[@itemprop="description"]/text()').extract_first(default='').strip()

        # address_list = response.xpath('//div[contains(@itemtype,"Organization")]'
        # '//div[@itemprop="address"]//text()').extract()
        address_list = response.xpath('//div[contains(@class,"visible-xs")]/div[@class="text"]//text()').extract()
        business['Address'] = ', '.join([i.strip() for i in address_list if i.strip()]).replace(
            ', ,', ',').replace(' , ', ', ').replace(',,', ',').strip()

        business['Phone'] = response.xpath('//span[@itemprop="telephone"]/text()').extract_first(default='').strip()

        business['Email'] = response.xpath('//span[@itemprop="email"]/text()').extract_first(default='').strip()

        business['Contact'] = response.xpath('//span[@itemprop="alumni"]/'
                                             'span[@itemprop="name"]/text()').extract_first(default='').strip()

        hours_list = response.xpath('//div[contains(@class,"working-hour-row")]//text()').extract()
        business['Hours'] = '_'.join([i.strip() for i in hours_list if i.strip()]).strip()

        description_list = response.xpath('//section[@id="about"]//text()').extract()
        business['Description'] = ' '.join([i.strip() for i in description_list if i.strip()]).strip()

        map_link = response.xpath('//a[@id="get_direct"]/@href').extract_first(default='')
        try:
            business['Latitude'] = map_link.split('=')[-1].split(',')[0]
            business['Longitude'] = map_link.split('=')[-1].split(',')[1]
        except Exception:
            business['Latitude'] = ''
            business['Longitude'] = ''

        business['Image_Url'] = response.xpath('//section[contains(@id,"info")]//img/@src').extract()
        if business['Name']:
            yield business
