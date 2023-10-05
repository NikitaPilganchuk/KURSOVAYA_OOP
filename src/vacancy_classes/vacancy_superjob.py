import json
from KURSOVAYA_OOP.src.vacancy_classes.vacancy import Vacancy

class VacancySJ(Vacancy):

    def __init__(self):
        self.params = {
            'keyword': None,
            'payment_from': None,
            'no_agreement': 1
            # 'experience': None,
        }

    def print_vacancies(self):
        with open('../vacancies_super_job.json', 'r', encoding='utf-8') as f:
            vacancies_list = json.load(f)
            vacancies_list = sorted(vacancies_list, key=lambda x: x['Зарплата'])
            num = 1
            for vacancy in vacancies_list:
                print(f'Вакансия No {num}')
                print(f"Должность: {vacancy['Должность']}")
                print(f"Зарплата от {vacancy['Зарплата']}")
                print(f"Ссылка: {vacancy['Ссылка']}")
                print(f"Обязанности: \n{vacancy['Обязанности']}")
                print()
                num += 1