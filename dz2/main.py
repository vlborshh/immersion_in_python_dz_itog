#Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими
# сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним,
# только если треугольник существует .
import logging
import argparse


logging.basicConfig(filename='Треугольник.log', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

def triangle(a: str, b: str, c : str) -> None:
    #a, b, c = input('Введите сторону a: '), input('Введите сторону b: '), input('Введите сторону c: ')
    if not (a.isdigit() and b.isdigit() and c.isdigit()):
        logger.error(f'Имеем: A = {a} B = {b} C = {c} - сторонами треугольника должны быть только цифры')
    else:
        a, b, c = int(a), int(b), int(c)
        if a + b < c or a + c < b or b + c < a:
            logger.info(f'Треугольника со сторонами: {a} {b} {c} не существует')
        elif a == b == c:
            logger.info(f'Треугольник со сторонами: A = {a}, B = {b}, C = {c} существует. Он равносторонний')
        elif a == b or b == c or a == c:
            logger.info(f'Треугольник со сторонами: A = {a}, B = {b}, C = {c} существует. Он равнобедренный')
        else:
            logger.info(f'Треугольник со сторонами: A = {a}, B = {b}, C = {c} существует. Он разносторонний')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Проверка на существование треугольника')
    parser.add_argument('sides_triangle', nargs=3, type=str, help='Вводится сторона А, B, C')
    args = parser.parse_args()
    # print(args.abc[0], args.abc[1], args.abc[2])
    triangle(args.sides_triangle[0], args.sides_triangle[1], args.sides_triangle[2])