from typing import Optional


def get_mask_card_number(card_number: Optional[str] = None) -> Optional[str]:
    """Функция  принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    blocks = []
    block_size = 4
    hidden_number = ""
    hide_number = [6, 7, 8, 9, 10, 11]
    for i, char in enumerate(card_number):
        if i in hide_number:
            hidden_number += "*"
        else:
            hidden_number += char
    for i in range(0, len(hidden_number), block_size):
        blocks.append(hidden_number[i : i + block_size])
    return " ".join(blocks)


def get_mask_account(account_number: Optional[str] = None) -> Optional[str]:
    """Функция принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX"""
    hidden_number = ""
    hide_number = [0, 1]
    for i, char in enumerate(account_number[-6:]):
        if i in hide_number:
            hidden_number += "*"
        else:
            hidden_number += char
    return hidden_number
