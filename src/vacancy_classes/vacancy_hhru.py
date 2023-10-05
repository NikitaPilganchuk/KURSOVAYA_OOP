import json
from KURSOVAYA_OOP.src.vacancy_classes.vacancy import Vacancy

class VacancyHHru(Vacancy):

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
        with open('../vacancies_HHru.json', 'r', encoding='utf-8') as f:
            vacancies_list = json.load(f)
            for vacancy in vacancies_list:
                print(f'Вакансия No {vacancy["Вакансия No"]}')
                print(f"Должность: {vacancy['Должность']}")
                print(f"Зарплата {vacancy['Зарплата']}")
                print(f"Требования: {vacancy['Требования']}")
                print(f"Обязанности: \n{vacancy['Обязанности']}")
                print()


