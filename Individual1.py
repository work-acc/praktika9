#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 5. Написать программу, которая считывает текст из файла и
# выводит его на экран, меняя местами каждые два соседних слова.

if __name__ == '__main__':
    with open('my.txt', 'r') as f:
        text = f.read()

    # Переставляем местами.
    sentences = text.split()
    x = sentences
    j = 0
    for i in range(int(len(x) / 2)):
        x[j], x[j + 1] = x[j + 1], x[j]
        j += 2
    print(x)
