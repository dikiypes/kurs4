import json
from abc import ABC, abstractmethod
import configprog
import requests


class abstrvacansy(ABC):    # абстрактные класс
    @abstractmethod
    def connect_api(self):
        pass
    @abstractmethod
    def download_vacancy(self):
        pass


class super_job(abstrvacansy):      # класс для работы с суперджобом
    def __init__(self):
        pass
    def connect_api(self):
        pass
    def download_vacancy(self):
        pass

class h_h(abstrvacansy):      # класс для работы с хедхантер
    def __init__(self):
        pass
    def connect_api(self):
        pass
    def download_vacancy(self,name,page):
        params = {
            'text': f'NAME:{name}',  # Текст фильтра. В имени должно быть слово "Аналитик"
            'area': 1,  # Поиск ощуществляется по вакансиям города Москва
            'page': page,  # Индекс страницы поиска на HH
            'per_page': 50  # Кол-во вакансий на 1 странице
        }

        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()
        vaclist = json.loads(data)['items']
        vaclistshort = []
        for vac in vaclist:
            name = vac["name"]
            url = vac["area"]["url"]
            if vac.get("salary"):
                zp_from = vac["salary"].get("from")
                zp_to = vac["salary"].get("to")
            else:
                zp_from = None
                zp_to = None
            rec = vac["snippet"]["requirement"]
            vaclistshort.append({"name": name, "url": url, "zp_from": zp_from, "zp_to": zp_to, "rec": rec})

        return vaclistshort

class save_info(ABC):
    @abstractmethod
    def write_info(self):
        pass
    @abstractmethod
    def dell_info(self):
        pass
    @abstractmethod
    def search_info(self):
        pass

class save_file(save_info):
    def __init__(self):
        pass
    def write_info(self):
        pass
    def dell_info(self):
        pass
    def search_info(self):
        pass


class vacansy:
    def __init__(self,name,url,zp_from,zp_to,rec):
        self.name = name
        self.url = url
        self.zp_from = zp_from
        self.zp_to = zp_to
        self.rec = rec
