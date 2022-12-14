#Вводятся два списка (каждый с новой строки) из слов, записанных через пробел. Имеется
#функция, которая преобразовывает эти две строки в два списка слов и возвращает эти
#списки. Определите декоратор для этой функции, который из этих двух списков
#формирует словарь, в котором ключами являются слова из первого списка, а значениями –
#соответствующие элементы из второго списка. Полученный словарь
#должен возвращаться при вызове декоратора. Примените декоратор к первой функции и
#вызовите ее. Результат (словарь) отобразите на экране.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # декоратор функции
    def decorator(func):
        def decorator_inside(A, B):
            data = func(A, B)
            return dict(zip(*data))

        return decorator_inside

    # основная функция + подключаем к ней декоратор
    @decorator
    def listing(A, B):
        return A.split(), B.split()


    First = input("Введите первую строку: ")
    Second = input("Введите вторую строку: ")
    print(listing(First, Second))
