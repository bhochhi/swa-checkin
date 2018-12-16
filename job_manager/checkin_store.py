import os

from flask import json


def load_scheduled_list():
    # filename = os.path.join(current_app.static_folder, 'data.json')
    if os.path.exists("data.json"):
        with open('data.json') as json_file:
            data = json.load(json_file)
            return data
    else:
        with open('data.json', 'w') as json_file:
            data = []
            json.dump(data, json_file)
            return data


def create_new_entry(data):
    full_list = load_scheduled_list()
    full_list.append(data)
    return update_scheduled_list(full_list)


def update_scheduled_list(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)
        return True
    return False


def delete_entry(data):
    full_list = load_scheduled_list()
    for p in full_list:
        if p['confirmationNumber'] == data.confirmationNumber:
            p.pop()
    return update_scheduled_list(full_list)
