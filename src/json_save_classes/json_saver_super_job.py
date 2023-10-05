from KURSOVAYA_OOP.src.json_save_classes.json_saver import JsonSaver
import json

class JsonSaverSJ(JsonSaver):

    def save(self, response):
        with open('../vacancies_super_job.json', 'w', encoding='utf-8') as f:
            vacancies_list = []
            num = 1
            for i in response.json()['objects']:
                vacancy = {
                                        'Вакансия No': num,
                                        'Должность': i['profession'],
                                        'Зарплата от': i['payment_from'],
                                        'Зарплата до': i['payment_to'],
                                        'Ссылка': i['link'],
                                        'Обязанности': i['candidat']
                }
                vacancies_list.append(vacancy)
                num += 1

            json.dump(vacancies_list, f)

    def delete_vacancy(self, vacancy_number):
        with open('../vacancies_super_job.json', 'r', encoding='utf-8') as f:
            vacancies_list = json.load(f)
            for i in vacancies_list:
                if i['Вакансия No'] == vacancy_number:
                    vacancies_list.remove(i)

        with open('../vacancies_super_job.json', 'w', encoding='utf-8') as f:
            json.dump(vacancies_list, f)


