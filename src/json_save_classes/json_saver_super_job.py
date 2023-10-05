from KURSOVAYA_OOP.src.json_save_classes.json_saver import JsonSaver
import json

class JsonSaverSJ(JsonSaver):

    def save(self, response):
        with open('../vacancies_super_job.json', 'w', encoding='utf-8') as f:
            vacancies_list = []
            num = 1
            for i in response.json()['objects']:
                middle = 0
                if i['payment_from'] and i['payment_to']:
                    middle = i['payment_from']
                elif i['payment_from'] and not i['payment_to']:
                    middle = i['payment_from']
                elif i['payment_to'] and not i['payment_from']:
                    middle = i['payment_to']
                vacancy = {
                                        'Вакансия No': num,
                                        'Должность': i['profession'],
                                        'Зарплата': middle,
                                        'Ссылка': i['link'],
                                        'Обязанности': i['candidat']
                }
                vacancies_list.append(vacancy)
                num += 1
                vacancies_list = sorted(vacancies_list, key=lambda x: x['Зарплата'])
            json.dump(sorted(vacancies_list, key=lambda x: x['Зарплата']), f)

    def delete_vacancy(self, vacancy_number):
        with open('../vacancies_super_job.json', 'r', encoding='utf-8') as f:
            vacancies_list = json.load(f)
            for i in vacancies_list:
                if i['Вакансия No'] == vacancy_number:
                    vacancies_list.remove(i)

        with open('../vacancies_super_job.json', 'w', encoding='utf-8') as f:
            json.dump(vacancies_list, f)


