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

def format_hide_transaction_from(text: str):
        transaction_from = text.split(" ")[-1]
        transaction_prefix = " ".join(text.split(" ")[0:-1]) + " "
        transaction_from_hide = transaction_from[0:6] + "*" * (len(transaction_from) - 10) + transaction_from[-4:]
        return transaction_prefix + " ".join(
            [transaction_from_hide[0 + 4 * i:4 + 4 * i] for i in range(0, int(len(transaction_from_hide) / 4), 1)])


def main():
    print(format_hide_transaction_from("Visa Classic 2842878893689012"))

