import scrapy
from douban.items import DoubanItem
from bs4 import BeautifulSoup
quanju=1

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # allowed_domains = ['douban.com/']
    # start_urls = ['https://movie.douban.com/top250']

    # allowed_domains = ['yx.tdsdyxly.com']
    # start_urls = ['https://yx.tdsdyxly.com/index']

    # allowed_domains = ['space.bilibili.com'] 
    # start_urls = ['https://space.bilibili.com/1629347259/video'] 
    # page = 10 # 如果想要爬取多页数据，需要定义爬取初始的页数，这里是1
    # # 后续页数的网址，需要自己观察翻页后网址的变化得出规律
    # base_url = 'https://space.bilibili.com/1629347259/video?tid=0&page={}'

    allowed_domains = ['prts.wiki/']
    start_urls = ['https://prts.wiki/id/1831']
    # page = 10 # 如果想要爬取多页数据，需要定义爬取初始的页数，这里是1
    # # 后续页数的网址，需要自己观察翻页后网址的变化得出规律
    # base_url = 'https://space.bilibili.com/1629347259/video?tid=0&page={}'

# index    //*[@id="filter-result"]/div[1]
# name     //*[@id="filter-result"]/div[1]/div[2]/div/div[1]
# cname    //*[@id="filter-result"]/div[1]/div[2]/div/a/div
# cname    //*[@id="filter-result"]/div[1]/div[2]/div/a/div
# hp       //*[@id="filter-result"]/div[1]/div[4]/div[1]
# atk      //*[@id="filter-result"]/div[1]/div[4]/div[2]
# re_ploy  //*[@id="filter-result"]/div[1]/div[5]/div[1]
# code     //*[@id="filter-result"]/div[1]/div[2]/div/div[3]
    def parse(self, response):

        ###### 下面是自己对html数据的处理逻辑
        
 
        movie_list = response.xpath("//*[@id=\"filter-result\"]/div")
        if movie_list and len(movie_list) > 0:
            for movie in movie_list:
                item = DoubanItem()
                item['cname'] = movie.xpath("normalize-space(./div[2]/div/a/div/text())").get()
                item['ename'] = movie.xpath("normalize-space(./div[2]/div/div[1]/text())").extract()[0]
                item['jname'] = movie.xpath("normalize-space(./div[2]/div/div[2]/text())").extract()[0]
                item['code'] = movie.xpath("normalize-space(./div[2]/div/div[3]/text())").extract()[0]
                item['sub_occupation'] = movie.xpath("normalize-space(./div[3]/div/div[1]/text())").extract()[0]
                item['influnce'] = movie.xpath("normalize-space(./div[3]/div/div[2]/text())").extract()[0]
                item['place_of_birth'] = movie.xpath("normalize-space(./div[3]/div/div[3]/text())").extract()[0]
                item['race'] = movie.xpath("normalize-space(./div[3]/div/div[4]/text())").extract()[0]
                item['hp'] = movie.xpath("normalize-space(./div[4]/div[1]/text())").get()
                item['atk'] = movie.xpath("normalize-space(./div[4]/div[2]/text())").extract()[0]
                item['defe'] = movie.xpath("normalize-space(./div[4]/div[3]/text())").extract()[0]
                item['res'] = movie.xpath("normalize-space(./div[4]/div[4]/text())").extract()[0]
                item['re_deploy'] = movie.xpath("normalize-space(./div[5]/div[1]/text())").extract()[0]
                item['cost'] = movie.xpath("normalize-space(./div[5]/div[2]/text())").extract()[0]
                item['block'] = movie.xpath("normalize-space(./div[5]/div[3]/text())").extract()[0]
                item['interval'] = movie.xpath("normalize-space(./div[5]/div[4]/text())").extract()[0]
                item['sex'] = movie.xpath("normalize-space(./div[6]/div[1]/text())").extract()[0]
                item['position'] = movie.xpath("normalize-space(./div[6]/div[2]/text())").extract()[0]
                item['obtain'] = [movie.xpath(f"normalize-space(./div[7]/div[{i}]/text())").get()
                                  for i in range(1,5)]
                item['tag'] = movie.xpath("normalize-space(./div[8]/div[1]/text())").get(),movie.xpath("normalize-space(./div[8]/div[2]/text())").extract()[0],movie.xpath("normalize-space(./div[8]/div[3]/text())").extract()[0],movie.xpath("normalize-space(./div[8]/div[4]/text())").extract()[0]
                item['feature'] = movie.xpath("normalize-space(./div[9]/div/div/text())").extract()[0]
                yield item
        next_link = response.xpath("//*[@id=\"pagination\"]/div[2]/div[2]/div[2]/@class").extract()

        # <div data-v-87b5d33f="" data-v-7bc26d06="" class="checkbox-container">2</div>
        # next_link = response.xpath("//*[@id='content']/div/div[1]/div[2]/a/@href").extract()
        if next_link:
            global quanju
            yield scrapy.Request('https://prts.wiki/id/1831' + next_link[2], callback=self.parse, dont_filter=True)
            quanju+=1
            # for i in range(len(next_link)):
            #     yield scrapy.Request("https://movie.douban.com/top250" + next_link[i], callback=self.parse, dont_filter=True)


            # scrapy crawl quotes -O quotes.json   运行指令