import json
import argparse


def load_data(file_path):
    try:
        with open(file_path, encoding='UTF8') as data_file:
            decoded_data = json.load(data_file)
            return decoded_data
    except ValueError:
        return None


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='Путь и имя .json файла')
    return parser


def pretty_print_json(decoded_data):
    print(
        json.dumps(
            decoded_data,
            ensure_ascii=False,
            sort_keys=True,
            indent=4
        )
    )


if __name__ == '__main__':
    script_argument = create_parser().parse_args()
    try:
        not_pretty_data = load_data(script_argument.file_path)
        if not_pretty_data is None:
            error = 'Данные в файле в неправильном формате'
            exit(error)
    except FileNotFoundError:
        error = '.json файл не найден!'
        exit(error)
    pretty_print_json(not_pretty_data)

