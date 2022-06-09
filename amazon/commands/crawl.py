from django.core.management.base import BaseCommand
from amazon.spiders.asin import AsinSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Command(BaseCommand):    
    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(AsinSpider)
        process.start()