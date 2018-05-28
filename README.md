# Красивый вывод JSON файла в консоль

После запуска скрипт выводит содержимое json файла в консоль в удобном для чтения виде: добавляет переносы строк, отступы слева и пробелы.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
а так же файл с данными в json формате. В параметрах при запуске скрипта необходимо 
передать путь и имя .json файла
Запуск на Linux:

```bash

$ python pprint_json.py alco_shops.json
# Пример ответа скрипта
"type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    37.81842699961744,
                    55.750829999765166
                ],
                "type": "Point"
            },
            "properties": {
                "Attributes": {
                    "Address": "Зелёный проспект, дом 60/35",
                    "AdmArea": "Восточный административный округ",
                    "ClarificationOfWorkingHours": null,
                    "District": "район Новогиреево",
                    "IsNetObject": "нет",
                    "Name": "МАГАЗИН «РОЗЛИВНОЕ ПИВО»",
                    "OperatingCompany": null,
                    "PublicPhone": [
                        {
                            "PublicPhone": "(495) 983-09-87"
                        }
                    ],
                    "TypeService": "реализация продовольственных товаров",
                    "WorkingHours": [
                        {
                            "DayOfWeek": "понедельник",
                            "Hours": "10:00-22:00"
                        },
                        {
                            "DayOfWeek": "вторник",
                            "Hours": "10:00-22:00"
                        },
                        {
                            "DayOfWeek": "среда",
                            "Hours": "10:00-22:00"
                        },
                        {
                            "DayOfWeek": "четверг",
                            "Hours": "10:00-22:00"
                        },
                        {
                            "DayOfWeek": "пятница",
                            "Hours": "10:00-22:00"
                        },
                        {
                            "DayOfWeek": "суббота",
                            "Hours": "10:00-22:00"
                        },
                        {
                            "DayOfWeek": "воскресенье",
                            "Hours": "10:00-22:00"
                        }
                    ],
                    "global_id": 25156884
                },
                "DatasetId": 1854,
                "ReleaseNumber": 2,
                "RowId": "10082733-a71f-4658-b4bf-8d1d86c30c37",
                "VersionNumber": 1
            },
            "type": "Feature"
        },

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
