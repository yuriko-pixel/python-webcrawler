from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["toscrape.com"]
    start_url = ["http://books.toscrape.com/"]
    
    rules = (
        Rule(LinkExtractor(allow="catalog/category")),
    )