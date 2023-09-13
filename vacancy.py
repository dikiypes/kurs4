class Vacancy:
    def __init__(self, vac_data: dict) -> None:
        self.name: str = vac_data.get('name', '')
        self.url: str = vac_data.get('url', '')
        self.zp_from: int = vac_data.get('zp_from', 0)
        self.zp_to: int = vac_data.get('zp_to', 0)
        self.rec: str = vac_data.get('rec', '')

    def __str__(self) -> str:
        result: str = f'{self.name} {self.zp_to} {self.zp_from} {self.rec}'
        return result

    def compare(self, other: 'Vacancy') -> str:
        '''Метод сравнения по зарплате. Возвращает вакансию с большей зарплатой или "равны".'''

        if self.zp_from != None and other.zp_from != None:
            if self.zp_from > other.zp_from:
                result: str = str(self.zp_from)
            elif self.zp_from < other.zp_from:
                result: str = str(other.zp_from)
            else:
                result: str = 'равны'
            return result
        else:
            print('нет возможность сравнить')
