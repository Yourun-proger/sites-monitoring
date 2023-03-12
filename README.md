# Мониторинг сайтов
Данный проект делает ровно то, что написано в ТЗ: получает csv файл с доменами/ip адресами и портами и проверяет их на доступность

Реализация - просто CLI приложение, однако это решение не так сложно перенести на web или gui
# Установка
Склонируйте себе репозиторий (или скачайте на прямую с github)
```bash
$ git clone https://github.com/Yourun-proger/sites-monitoring.git
```
Выполните команду:
```bash
$ pip install -e .
```
Поздравляю, вы справились с установкой!
# Использование
Введите в командной строке:
```bash
$ monitoring_report PATH_TO_CSV_FILE
```
где вместо `PATH_TO_CSV_FILE` собственно надо написать путь к csv файлу

Это всё!