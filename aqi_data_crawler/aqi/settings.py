# -*- coding: utf-8 -*-

# Scrapy settings for aqi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'aqi'

SPIDER_MODULES = ['aqi.spiders']
NEWSPIDER_MODULE = 'aqi.spiders'
MEDIA_ALLOW_REDIRECTS = True
ITEM_PIPELINES = {'aqi.pipelines.AQIPipeline': 1}
FILES_STORE = r'/download'
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 0.5
CONCURRENT_REQUESTS = 16
AUTOTHROTTLE_ENABLED = True
