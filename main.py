from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card
from src.widget import get_date
#numbers = input("Введите 16 чисел")
#print(get_mask_card_number(numbers))

#numbers = input("Введите 16 чисел")
#print(get_mask_account(numbers))

#numbers = 'Visa Classic 6831982476737658'
numbers = 'Счет 64686473678894779589'
print(mask_account_card(numbers))

raw_date = "2024-03-11T02:26:18.671407"
print(get_date(raw_date))
