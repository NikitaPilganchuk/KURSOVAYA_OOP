from KURSOVAYA_OOP.src.api_classes.super_job_api import SuperjobAPI
from KURSOVAYA_OOP.src.api_classes.head_hunter_api import HeadHunterAPI
from KURSOVAYA_OOP.src.json_save_classes.json_saver_hhru import JsonSaverHHru
from KURSOVAYA_OOP.src.json_save_classes.json_saver_super_job import JsonSaverSJ
from KURSOVAYA_OOP.src.vacancy_classes.vacancy_hhru import VacancyHHru
from KURSOVAYA_OOP.src.vacancy_classes.vacancy_superjob import VacancySJ



def user_interaction():
    flag = True
    while flag == True:
        print("Выберите пункт меню:")
        print("1.Искать вакансии на HH.ru")
        print("2.Искать вакансии на SuperJob.ru")
        print("3.Выход")
        user_input = input("Ваш выбор: ")
        if user_input == '1':
            user_input = input("Введите ключевое слово для поиска вакансии: ")
            user_vacancy_search = HeadHunterAPI()
            user_vacancy_search.params['text'] = user_input
            while True:
                user_input = input("\nВведите минимальную зарплату: \nВаш выбор: ")
                if user_input.isdigit() == True:
                    user_vacancy_search.params['salary_from'] = int(user_input)
                    break
                else:
                    print("Неверный ввод")
            while True:
                user_input = input('Введите количество вакансий для поиска(Максимум 30): \nВаш выбор: ')
                if user_input.isdigit() == True and int(user_input) < 31:
                    user_vacancy_search.params['per_page'] = int(user_input)
                    user_vacancy_json = JsonSaverHHru()
                    user_vacancy_json.save(user_vacancy_search.get_vacancies())
                    user_vacancy = VacancyHHru()
                    user_vacancy.print_vacancies()
                    break
                else:
                    print("Неверный ввод")
            while True:
                user_input = input("\nЖелаете удалить какую-либо вакансию? (y/n)")
                if user_input == 'y':
                    user_input = input("Введите номер вакансии для удаления: ")
                    if user_input.isdigit() == True:
                        user_vacancy_json.delete_vacancy(int(user_input))
                        user_vacancy.print_vacancies()
                        continue
                    else:
                        print("Неверный ввод")
                else:
                    break


            user_input = input("\nЖелаете продолжить поиск вакансий? (y/n)")
            if user_input == 'y':
                continue
            elif user_input == 'n':
                flag = False
            else:
                print('Неверный ввод')


        elif user_input == '2':
            user_input = input("Введите ключевое слово для поиска вакансии: ")
            user_vacancy_search = SuperjobAPI()
            user_vacancy_search.params['keyword'] = user_input
            while True:
                user_input = input("\nВведите минимальную зарплату: \nВаш выбор: ")
                if user_input.isdigit() == True:
                    user_vacancy_search.params['payment_from'] = int(user_input)
                    user_vacancy_json = JsonSaverSJ()
                    user_vacancy_json.save(user_vacancy_search.get_vacancies())
                    user_vacancy = VacancySJ()
                    user_vacancy.print_vacancies()
                    break
                else:
                    print("Неверный ввод")
            while True:
                user_input = input("\nЖелаете удалить какую-либо вакансию? (y/n)")
                if user_input == 'y':
                    user_input = input("Введите номер вакансии для удаления: ")
                    if user_input.isdigit() == True:
                        user_vacancy_json.delete_vacancy(int(user_input))
                        user_vacancy.print_vacancies()
                        continue
                    else:
                        print("Неверный ввод")
                else:
                    break
            user_input = input("\nЖелаете продолжить поиск вакансий? (y/n)\n")
            if user_input == 'y':
                continue
            elif user_input == 'n':
                flag = False
            else:
                print('Неверный ввод\n')
        elif user_input == '3':
            flag = False



if __name__ == '__main__': user_interaction()
