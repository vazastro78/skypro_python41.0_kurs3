#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime


'''
Функция принимает на входе строку, которая представляет собой iso запись даты,
на выходе преобразует в вид 23.02.2019
использует библиотеку datetime
'''
def format_date(text: str):
    dt = datetime.fromisoformat(text)
    return dt.strftime("%d.%m.%Y")


def main():
    print(format_date("2019-12-08T22:46:21.935582"))

