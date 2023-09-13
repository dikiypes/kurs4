from abstracts_class import AbstractAPI
import requests
import config
import json
from typing import List, Dict, Any, Optional

class HeadHunterAPI(AbstractAPI):
    """
    Класс для получения информации от API HeadHunter
    """
    def __init__(self) -> None:
        pass

    def get_vacancy_page(self, name: str, page: int) -> List[Dict[str, Any]]:
        self.params = {
            'text': f'NAME:{name}',
            'area': 1,
            'page': page,
            'per_page': 50
        }
        req = requests.get('https://api.hh.ru/vacancies', params=self.params)
        data = req.content.decode()
        vaclist = json.loads(data)['items']
        vaclistshort = []
        for vac in vaclist:
            id = vac['id']
            name = vac["name"]
            url = vac["area"]["url"]
            if vac.get("salary"):
                zp_from = vac["salary"].get("from")
                zp_to = vac["salary"].get("to")
            else:
                zp_from = None
                zp_to = None
            rec = vac["snippet"]["requirement"]
            vaclistshort.append({"id": id,"name": name, "url": url, "zp_from": zp_from, "zp_to": zp_to, "rec": rec})

        return vaclistshort

class SuperJobAPI(AbstractAPI):
    """
    Класс для получения информации от API SuperJob
    """
    def __init__(self) -> None:
        self.headers = {
            'X-Api-App-Id': config.sj_api_key,
        }

    def get_vacancy_page(self, name: str, page: int) -> List[Dict[str, Any]]:
        params = {
            'keyword': name,
            'count': 50,  # Количество вакансий для вывода
            'page': 1,  # Номер страницы
        }
        base_url = 'https://api.superjob.ru/2.0/'
        endpoint = 'vacancies/'
        req = requests.get(base_url + endpoint, params=params, headers=self.headers)
        vaclistshort = []
        if req.status_code == 200:
            data = req.content.decode()
            vaclist = json.loads(data)['objects']
            print(vaclist)
            for vac in vaclist:
                id = vac['id']
                name = vac['profession']
                url = vac['link']
                zp_from = vac['payment_from']
                zp_to = vac['payment_to']
                rec = vac['candidat']
                vaclistshort.append({"id": id,"name": name, "url": url, "zp_from": zp_from, "zp_to": zp_to, "rec": rec})
        return vaclistshort
