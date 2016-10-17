import json


def load_data(filepath):
    with open(filepath, 'r', encoding="UTF-8" ) as handle:
        data = json.load(handle)
        return data


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, separators=(',', ':'), ensure_ascii=False))


if __name__ == '__main__':
    data = input("введите путь до файла!n/")
    pretty_print_json(load_data(data))
