import json
import argparse


def load_data(file_path):
    try:
        with open(file_path, encoding='UTF8') as data_file:
            file_data = json.load(data_file)
            return file_data
    except ValueError:
        return None


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='Путь и имя .json файла')
    return parser


def pretty_json(file_data):
    return json.dumps(file_data, ensure_ascii=False, sort_keys=True, indent=4)


if __name__ == '__main__':
    script_argument = create_parser().parse_args()
    try:
        loaded_data = load_data(script_argument.file_path)
        if loaded_data is None:
            error = 'Данные в файле в неправильном формате'
            exit(error)
    except FileNotFoundError:
        error = '.json файл не найден!'
        raise FileNotFoundError(error)
    print(pretty_json(loaded_data))

