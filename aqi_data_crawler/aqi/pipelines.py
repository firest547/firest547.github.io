# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to t he ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
import os
import pathlib
import re
import subprocess


class AQIPipeline(FilesPipeline):
    def process_item(self, item, spider):
        url = item["file_urls"][-1]
        file_name = re.split(r'Data\-Donnees\/', url)[-1]
        path = pathlib.Path(file_name).parent
        path = os.path.join('download', path)

        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)

        subprocess.call(['wget', '-nH', item["file_urls"][-1],
                         f'-P{path}'])
