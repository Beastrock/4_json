import json
import os.path


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding="UTF-8") as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    print(json.dumps
          (data, indent=4, sort_keys=True,
           separators=(',', ':'), ensure_ascii=False))


if __name__ == '__main__':
    json_filepath = input("Введите путь до файла или сам файл,"
                          " если он находится в этой директории:\n")
    pretty_print_json(load_data(json_filepath))
