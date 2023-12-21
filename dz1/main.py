# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем. На вход будет подаваться
# дата в формате "день.месяц.год". Ваша задача - создать программу, которая проверяет, является ли введенная дата
# корректной или нет.

from datetime import date
import logging
import argparse


logging.basicConfig(filename='Проверка даты.log', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)
def check_date(date_to_prove):

    day, month, year = date_to_prove.split('.')
    if not (day.isdigit() or month.isdigit() or year.isdigit()):
        logger.error(f'В {date_to_prove} должны быть только цифры')
        return False

    day = int(day)
    month = int(month)
    year = int(year)

    try:
        date(year, month, day)
        logger.info(f'Введено: {date_to_prove}. Все верно')
        return True
    except:
        logger.error(f'Введено: {date_to_prove}. Такой даты не существует')
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Проверка корректности даты')
    parser.add_argument('date', nargs=1, type=str, help='Вводится строка вида: дд.мм.гггг')
    args = parser.parse_args()
    date_to_prove = args.date[0]
    print(check_date(date_to_prove))