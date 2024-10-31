# модуль processing содержит функции обработки данных

from typing import Any


def filter_by_state(list_dict: list[dict[str, Any]], def_state: str = 'EXECUTED') -> list[dict[str, Any]]:
    '''Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению '''
    new_list_dict = []
    for dict_id in list_dict:
        if dict_id.get('state') == def_state:
            new_list_dict.append(dict_id)
    return new_list_dict


def sort_by_date(list_dict: list[dict[str, Any]], def_state: bool = True) -> list[dict[str, Any]]:
    '''Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате'''
    return sorted(list_dict, key=lambda dict_id: dict_id.get('date'), reverse=def_state)
