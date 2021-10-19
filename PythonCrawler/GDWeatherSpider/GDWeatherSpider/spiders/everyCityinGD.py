import scrapy
from urllib.request import urlopen
import urllib.request
from re import findall
from GDWeatherSpider.items import GdweatherspiderItem

class EverycityingdSpider(scrapy.Spider):
    name = 'everyCityinGD'
    allowed_domains = ['www.weather.com.cn']
    start_urls = []
    # 遍历各城市，获取要爬取的页面URL
    url = r'http://www.weather.com.cn/guangdong/index.shtml'
    with urlopen(url) as fp:
        contents = fp.read().decode()
    pattern = '<a title=".*?" href="(.+?)" target="_blank">(.+?)</a>'
    for url in findall(pattern, contents):
        start_urls.append(url[0])

    def parse(self, response):
        item = GdweatherspiderItem()
        city = response.xpath('//div[@class="crumbs fl"]//a[3]//text()').extract()[0]
        item['city'] = city

        selector = response.xpath('//ul[@class="t clearfix"]')[0]

        weather = ''
        for li in selector.xpath('./li'):
            date = li.xpath('./h1//text()').extract()[0]
            cloud = li.xpath('./p[@title]//text()').extract()[0]
            high = li.xpath('./p[@class="tem"]//span//text()').extract()
            if high:
                high = high[0]
            else:
                high = 'none'
            low = li.xpath('./p[@class="tem"]//i//text()').extract()[0]
            wind = li.xpath('./p[@class="win"]//em//span[1]/@title').extract()[0]
            wind += li.xpath('./p[@class="win"]//i//text()').extract()[0]
            weather = weather + date + ':' + cloud + ',' + high + '/' + low + ',' + wind + '\n'
        item['weather'] = weather
        return [item]

