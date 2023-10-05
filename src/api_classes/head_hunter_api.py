from KURSOVAYA_OOP.src.api_classes.abstract_class_api import AbstractClassAPI
import requests


class HeadHunterAPI(AbstractClassAPI):
    '''
    Класс по поиску вакансий на сайте HH
    '''

    def __init__(self):
        self.params = {
            'text': None,
            "area": 1,  # (1 is Moscow)
            "per_page": None,
            'salary_from': None,
            'only_with_salary': True,
            # 'experience': None,
        }

    @property
    def text(self):
        return self.params['text']

    @property
    def salary_from(self):
        return self.params['salary_from']

    @property
    def per_page(self):
        return self.params['per_page']

    def get_vacancies(self):
        print(self.params)

        response = requests.get('https://api.hh.ru/vacancies', params=self.params)
        if response.status_code == 200:
            print('Запрос получен успешно')
        else:
            print(f"Request failed with status code: {response.status_code}")
        return response




