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


def format_hide_transaction_to(text: str):
    transaction_to = text.split(" ")[-1]
    transaction_prefix = " ".join(text.split(" ")[0:-1]) + " "
    transaction_to_hide = "*" * (len(transaction_to) - 4) + transaction_to[-4:]
    # print(transaction_to)
    return transaction_prefix + transaction_to_hide

def format_transaction(transaction: dict):
        return """
{date_formated} {description}
{from_hide} -> {to_hide}
{sum}

""".format(**transaction)

def get_sorted_top(keys,amount=5):
    return sorted( list(keys),  reverse=True)[0:amount]

def construct_transaction(item: dict):
        transaction = {}
        transaction["date_formated"] = format_date(item["date"])
        try:
            transaction["from_hide"] = format_hide_transaction_from(item["from"])
        except:
            transaction["from_hide"] = "неизвестный отправитель"
        try:
            transaction["to_hide"] = format_hide_transaction_to(item["to"])
        except:
            transaction["to_hide"] = "неизвестный получатель"
        transaction["description"] = item["description"]
        transaction["sum"] = item["operationAmount"]["amount"] + " " + item["operationAmount"]["currency"]["name"]
        return transaction


def get_executed_transactions(json_data):
    transaction_dict = {}
    for item in  json_data:
        try:
            if item["state"]=="EXECUTED":
                transaction_dict[ item["date"] ] = item
        except:
            pass
    return transaction_dict


def main():
    json_data = [
        {'date': '2019-10-01', 'state': 'EXECUTED'},
        {'date': '2010-01-01', 'state': 'CANCELED'}
    ]
    print(get_executed_transactions(json_data))

