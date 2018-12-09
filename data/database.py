import json


def get_timetable():
    with open('data/timetable.txt') as data_file:
        data = json.load(data_file)
    return data