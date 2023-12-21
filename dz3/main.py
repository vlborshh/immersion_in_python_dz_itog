# Напишите код, который анализирует число num и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если это число натуральное и делится нацело только на
# единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. Если подается отрицательное число или
# число более ста тысяч, выведите на экран сообщение: "Число должно быть больше 1 и меньше 100000".

import logging
import argparse


logging.basicConfig(filename='Число.log', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

#a = input('Введите число: ')

def simple_compound_number(a: str) -> None:
    if not a.isdigit():
        logger.error(f'На вход должны подаваться только цифры')
    else:
        num = int(a)
        if num < 2 or num > 100000:
            logger.info('Число должно быть больше 1 и меньше 100000')
        else:
            n = num
            counter = 0
            i = 3
            for i in range(1, n + 1):
                if n % i == 0:
                    counter += 1
            if counter < 3:
                logger.info(f'{num} является простым числом')
            else:
                logger.info(f'{num} является составным числом')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Анализируем число и сообщаем является ли оно простым или составным')
    parser.add_argument('a', nargs=1, type=str, help='Вводится число')
    args = parser.parse_args()
    # print(args.abc[0], args.abc[1], args.abc[2])
    simple_compound_number(args.a[0])