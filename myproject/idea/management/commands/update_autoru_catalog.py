from typing import Any
from django.core.management.base import BaseCommand
import requests, logging
from bs4 import BeautifulSoup as bs
from idea.models import CarMark, CarModel


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Add all marks and models for car'

    def handle(self, *args: Any, **options: Any):
        CarMark.objects.all().delete()
        CarModel.objects.all().delete()
        URL_TEMPLATE = 'https://auto-export.s3.yandex.net/auto/price-list/catalog/cars.xml'
        r = requests.get(URL_TEMPLATE)
        logger.info(f'{r.status_code}')
        soup = bs(r.text, features='xml')
        for mark in soup.find_all('mark'):
            car_mark = CarMark(name=mark['name'])

            temp_set = set()
            for model in mark.find_all('folder'):
                temp_set.add(model['name'].split(',')[0])
            for i in temp_set:
                car_model = CarModel(name=i, carmark=car_mark)

            temp_set.clear()