import datetime
import csv


def write_csv(user: str, arg1, arg2, result, file_name: str = 'dev_data.csv') -> None:
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{datetime.datetime.now()}|{user}|{arg1}|{arg2}|{result}\n')


def read_csv(file_name: str = 'dev_data.csv') -> list:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = csv.DictReader(file, ['date', 'user', 'arg1', 'arg2', 'result'], delimiter='|')
        return list(data)


def add_two_numbers(first: int | float, second: int | float) -> int | float:
    return first + second
