import json
import sys

def main():
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]
    
    with open(values_file, 'r') as f:
        values_data = json.load(f)

    values_dict = {}

    for item in values_data['values']:
        values_dict[item['id']] = item['value']
    
    with open(tests_file, 'r') as f:
        tests_data = json.load(f)

    def values(data):
        # если это список, то отправляем его рекурсивно в функцию
        if isinstance(data, list):

            for item in data:
                values(item)
        # если это словарь, достаем данные
        elif isinstance(data, dict):

            if 'id' in data and data['id'] in values_dict:
                data['value'] = values_dict[data['id']]

            for key, value in data.items():

                if key == 'values' and isinstance(value, list):
                    values(value)

                elif isinstance(value, (dict, list)):
                    values(value)

    values(tests_data['tests'])

    with open(report_file, 'w') as f:
        json.dump(tests_data, f, indent=2)

    print("Report.json создан")

if __name__ == "__main__":
    main()