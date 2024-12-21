# Домашняя работа по модулю DJANGO

## Описание.
Создан проект интернет-магазина MoS c помощью Django. 
Проект содержит приложения blogs, catalog, config, users.

## Папки, пакеты, приложения, шаблоны реализованные в проекте.
1. приложения:
- blogs;
- catalog; 
- config - содержит настройки Django проекта;
- users;
2. fixtures - файлы json;
3. static - содержит css и js настройки для Bootstrap;
4. media - картинки для сайта.

## Используемые зависимости.

asgiref==3.8.1
asttokens==3.0.0
black==24.10.0
certifi==2024.12.14
charset-normalizer==3.4.0
click==8.1.7
coverage==7.6.9
decorator==5.1.1
Django==5.1.4
django-phonenumber-field==8.0.0
django-redis==5.4.0
et_xmlfile==2.0.0
executing==2.1.0
flake8==7.1.1
idna==3.10
iniconfig==2.0.0
ipython==8.31.0
isort==5.13.2
jedi==0.19.2
matplotlib-inline==0.1.7
mccabe==0.7.0
mypy==1.13.0
mypy-extensions==1.0.0
numpy==2.2.0
openpyxl==3.1.5
packaging==24.2
pandas==2.2.3
parso==0.8.4
pathspec==0.12.1
pexpect==4.9.0
pillow==11.0.0
platformdirs==4.3.6
pluggy==1.5.0
prompt_toolkit==3.0.48
psycopg2-binary==2.9.10
ptyprocess==0.7.0
pure_eval==0.2.3
pycodestyle==2.12.1
pyflakes==3.2.0
Pygments==2.18.0
pytest==8.3.4
pytest-cov==5.0.0
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
pytz==2024.2
redis==5.2.1
requests==2.32.3
six==1.17.0
sqlparse==0.5.3
stack-data==0.6.3
traitlets==5.14.3
types-psycopg2==2.9.21.20240819
types-requests==2.32.0.20240914
typing_extensions==4.12.2
tzdata==2024.2
urllib3==2.2.3
wcwidth==0.2.13


## Установка

1. Клонируйте репозиторий:
'''
git clone https://github.com/SergeiVokhminov/django_homework.git
'''

2. Установите зависимости:
```
poetry install
```
или
```
pip install -r requirements.txt
```

## Тестирование:

1. в данном домашнем задании тестирование не предусмотренно.

## Использование модуля main.py:

1. Откройте модуль
2. Запустите if __name__ == "__main__"

## Документация

Для получения дополнительной информации обратитесь к [документации](README.md)