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
{
  "features": [
    {
      "geometry": {
        "coordinates": [
          37.39703804817934,
          55.740999719549094
        ],
        "type": "Point"
      },
      "properties": {
        "DatasetId": 1854,
        "VersionNumber": 1,
        "ReleaseNumber": 2,
        "RowId": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Attributes": {
          "global_id": 14371450,
          "Name": "Ароматный Мир",
          "IsNetObject": "да",
          "OperatingCompany": "Ароматный Мир",
          "TypeService": "реализация продовольственных товаров",
          "AdmArea": "Западный административный округ",
          "District": "район Кунцево",
          "Address": "улица Академика Павлова, дом 10",
          "PublicPhone": [
            {
              "PublicPhone": "(495) 777-51-95"
            }
          ],
          "WorkingHours": [
            {
              "Hours": "09:30-22:30",
              "DayOfWeek": "понедельник"
            },
            {
              "Hours": "09:30-22:30",
              "DayOfWeek": "вторник"
            },
            {
              "Hours": "09:30-22:30",
              "DayOfWeek": "среда"
            },
            {
              "Hours": "09:30-22:30",
              "DayOfWeek": "четверг"
            },
            {
              "Hours": "09:30-22:30",
              "DayOfWeek": "пятница"
            },
            {
              "Hours": "09:30-22:30",
              "DayOfWeek": "суббота"
            },
            {
              "Hours": "09:30-22:30",
              "DayOfWeek": "воскресенье"
            }
          ],
          "ClarificationOfWorkingHours": null
        }
      },
      "type": "Feature"
    }
  ],
  "type": "FeatureCollection"
}


# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
