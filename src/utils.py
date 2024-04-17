#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import json
import os


'''
Функция принимает на входе строку, которая представляет собой iso запись даты,
на выходе преобразует в вид 23.02.2019
использует библиотеку datetime
'''
def format_date(text: str):
    dt = datetime.fromisoformat(text)
    return dt.strftime("%d.%m.%Y")


def load_operations(filename="operations.json", datadir="data"):
    operations = {}
    full_filename = os.path.join(".", datadir, filename)
    with open(full_filename) as fp:
        json_data = json.load(fp)
    return json_data


def main():
    print(load_operations(filename="operations.json"))

