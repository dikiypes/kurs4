from api_platforms_class import HeadHunterAPI, SuperJobAPI
from vacancy import Vacancy
from file_class import JSON_File


def main() -> None:
    """
    Главная функция для выполнения запросов и сравнения вакансий.

    Функция позволяет пользователю выбрать платформу (HeadHunter или SuperJob),
    ввести название вакансии и номер страницы для получения вакансий. Затем
    пользователь может просмотреть список вакансий, сравнить две вакансии по
    зарплате и сохранить результаты в файл JSON.

    """
    print('1. HeadHunter')
    print('2. SuperJob')
    platforms_choice = int(input('Выберите платформу (1, 2): '))
    vac_name = input('Введите название вакансии: ')
    print('За один запрос Вы можете получить одну страницу вакансий.')
    print('Одна страница содержит до 50 вакансий')
    vac_page = input('Введите номер страницы, которую хотите получить: ')
    print()

    if platforms_choice == 1:
        platform = HeadHunterAPI()
    elif platforms_choice == 2:
        platform = SuperJobAPI()

    vac_list = platform.get_vacancy_page(vac_name, vac_page)
    for number, vac in enumerate(vac_list):
        print(number, end=' ')
        for key, value in vac.items():
            print(f'{key} : {value}', end=' ')
        print()

    print()

    while True:
        sample = input('Для сравнения вакансий по зарплате введите их номера через пробел или оставьте поле пустым для пропуска сравнения: ')
        if sample:
            sample = sample.split()
            if 0 < int(sample[0]) < 50 and 0 < int(sample[1]) < 50:
                vac_1 = Vacancy(vac_list[int(sample[0])])
                vac_2 = Vacancy(vac_list[int(sample[1])])
                sample_result = vac_1.compare(vac_2)

                print('Результат сравнения:', sample_result)
            else:
                print('ошибка номера вакансии')
        else:
            break

    save = input('Хотите сохранить результат в файл (y / n): ')
    if save == 'y':
        if platforms_choice == 1:
            js_saver = JSON_File('hh_vacancies.json')
        elif platforms_choice == 2:
            js_saver = JSON_File('sj_vacancies.json')
        js_saver.save(vac_list)

if __name__ == '__main__':
    main()
