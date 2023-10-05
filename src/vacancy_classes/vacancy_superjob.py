import json
from KURSOVAYA_OOP.src.vacancy_classes.vacancy import Vacancy

class VacancySJ(Vacancy):

    def __init__(self):
        self.params = {
            'text': None,
            "area": 1,  # (1 is Moscow)
            "per_page": None,
            'salary_from': None,
            'only_with_salary': True,
            # 'experience': None,
        }

    def print_vacancies(self):
        with open('../vacancies_super_job.json', 'r', encoding='utf-8') as f:
            vacancies_list = json.load(f)
            for vacancy in vacancies_list:
                print(f'Вакансия No {vacancy["Вакансия No"]}')
                print(f"Должность: {vacancy['Должность']}")
                print(f"Зарплата от {vacancy['Зарплата от']} до {vacancy['Зарплата до']}")
                print(f"Ссылка: {vacancy['Ссылка']}")
                print(f"Обязанности: \n{vacancy['Обязанности']}")
                print()