from KURSOVAYA_OOP.src.api_classes.abstract_class_api import AbstractClassAPI
import requests
import os
import json

class SuperjobAPI(AbstractClassAPI):

    API_URL = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self):
        self.params = {
            'keyword': None,
            'payment_from': None,
            'no_agreement': 1
        }
        self.headers = {
            'X-Api-App-Id': os.getenv('SuperJob')
        }
    @property
    def keyword(self):
        return self.params['keyword']

    @property
    def payment_from(self):
        return self.params['payment_from']

    def get_vacancies(self):
        response = requests.get(self.API_URL, params=self.params, headers=self.headers)
        return response





