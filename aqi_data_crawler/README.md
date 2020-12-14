# Crawler: Data-Donnees AQI data

This Scrapy based crawler downloads data from the Government of Canada's open data repository, [Data-Donnees](http://data.ec.gc.ca/data/air/monitor/national-air-pollution-surveillance-naps-program/Data-Donnees/?lang=en).

## Requirements
This package is based on Python 3.7 and Scrapy 2.4.1. To install Scrapy, run:
```pip install Scrapy==2.4.1```

## How to use
Specify the download directory path on ```aqi/settings.py```:
```FILES_STORE = r'<download_directory_path>'```

To run, use:
```scrapy crawl aqi```
