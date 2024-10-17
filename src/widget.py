from typing import Optional
from src.masks import get_mask_card_number


def mask_account_card(account_card_number: Optional[str] = None) -> Optional[str]:
    """Функция  которая умеет обрабатывать информацию как о картах,
    так и о счетах.
    # Пример для карты
    Visa Platinum 7000792289606361  # входной аргумент
    Visa Platinum 7000 79** **** 6361  # выход функции
    # Пример для счета
    Счет 73654108430135874305  # входной аргумент
    Счет **4305  # выход функции"""
    temp_list = account_card_number.split(" ")
    if len(temp_list[-1]) > 16:
        account_number = temp_list.pop(-1)
        account_number = f'**{account_number[-5:-1]}'
        temp_list.append(account_number)
    else:
        card_number = temp_list.pop(-1)
        card_number = get_mask_card_number(card_number)
        temp_list.append(card_number)
    return ' '.join(temp_list)


def get_date(raw_date: Optional[str] = None) -> Optional[str]:
    """Функция которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407" и возвращает строку с датой в
    формате "ДД.ММ.ГГГГ" ("11.03.2024")"""
    return f"{raw_date[8:10]}.{raw_date[5:7]}.{raw_date[:4]}"
