from src.masks import get_mask_account, get_mask_card_number

numbers = input("Введите 16 чисел")
print(get_mask_card_number(numbers))

numbers = input("Введите 16 чисел")
print(get_mask_account(numbers))
