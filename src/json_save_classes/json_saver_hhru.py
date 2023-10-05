from KURSOVAYA_OOP.src.json_save_classes.json_saver import JsonSaver
import json

class JsonSaverHHru(JsonSaver):

    def save(self, response):
        with open('../vacancies_HHru.json', 'w', encoding='utf-8') as f:
            vacancies_list = []
            for i in response.json()['items']:
                middle = 0
                if i['salary']['from'] and i['salary']['to']:
                    middle = i['salary']['from']
                elif i['salary']['from'] and not i['salary']['to']:
                    middle = i['salary']['from']
                elif i['salary']['to'] and not i['salary']['from']:
                    middle = i['salary']['to']
                vacancy = {
                    'Зарплата': middle,
                    'Должность': i['name'],
                    'Требования': i['snippet']['requirement'],
                    'Обязанности': i['snippet']['responsibility']
                }
                vacancies_list.append(vacancy)
            json.dump(sorted(vacancies_list, key=lambda x: x['Зарплата']), f)

    def delete_vacancy(self, vacancy_number):
        with open('../vacancies_HHru.json', 'r', encoding='utf-8') as f:
            vacancies_list = json.load(f)
            for i in vacancies_list:
                if i['Вакансия No'] == vacancy_number:
                    vacancies_list.remove(i)

        with open('../vacancies_HHru.json', 'w', encoding='utf-8') as f:
            json.dump(vacancies_list, f)