from abc import ABC, abstractmethod
class Vacancy(ABC):

    @abstractmethod
    def print_vacancies(self):
        pass

