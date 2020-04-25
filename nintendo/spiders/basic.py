# -*- coding: utf-8 -*-
import json
import socket
from datetime import datetime

import scrapy
from scrapy.mail import MailSender

from nintendo.items import MachineItem


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['store.nintendo.co.jp']
    start_urls = ['https://store.nintendo.co.jp/item/HAD_S_KAYAA.html']

    def parse(self, response):
        self.log('price %s' % response.xpath('//*[@id="HAD_S_KAYAA"]/p[@class="price"]/text()').extract())
        self.log('unit %s' % response.xpath('//*[@id="HAD_S_KAYAA"]/p[@class="price"]/span/text()').extract())
        self.log('stock %s' % response.xpath('//*[@id="HAD_S_KAYAA"]/p[@class="stock"]/text()').extract())
        self.log('costFree %s' % response.xpath('//*[@id="HAD_S_KAYAA"]/p[3]/text()').extract())
        self.log('pointPresent %s' % response.xpath('//*[@id="HAD_S_KAYAA"]/p[4]/text()').extract())

        mitem = MachineItem()
        mitem['url'] = response.url
        mitem['price'] = response.xpath('//*[@id="HAD_S_KAYAA"]/p[@class="price"]/text()').extract()
        mitem['unit'] = response.xpath('//*[@id="HAD_S_KAYAA"]/p[@class="price"]/span/text()').extract()
        mitem['stock'] = response.xpath('//*[@id="HAD_S_KAYAA"]/p[@class="stock"]/text()').extract()
        mitem['costFee'] = response.xpath('//*[@id="HAD_S_KAYAA"]/p[@class="cost_free"]/text()').extract()
        mitem['pointPresent'] = response.xpath('//*[@id="HAD_S_KAYAA"]/p[@class="point_present"]/text()').extract()
        mitem['timestamp'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        mitem['server'] = socket.gethostname()

        # # 将结果邮件发送
        # mailer = MailSender(smtphost='smtp.126.com',
        #                     mailfrom='nchufujianjian@126.com',
        #                     smtpuser='nchufujianjian@126.com',
        #                     smtppass='fujianjian007',
        #                     smtpport=25,
        #                     smtptls=False,
        #                     smtpssl=False
        #                     )
        # mailer.send(to='nchufujianjian@126.com',
        #             subject='Scrapy project test mail',
        #             body='Scrapy project test mail\n' + json.dumps(mitem)
        #             )
        return mitem
        # pass
