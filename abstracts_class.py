from abc import ABC, abstractmethod

class AbstractAPI(ABC):
    """Абстрактный класс для работы с API """

    @abstractmethod
    def get_vacancy_page(self, name, page):
        pass

class FileVacancy(ABC):
    """Абстрактный класс для работы с файлами вакансий вакансий"""

    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def get_by_name(self):
        pass

    @abstractmethod
    def del_by_id(self):
        pass
