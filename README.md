## Описание проекта

API сервис для проекта социальной сети Yatube.

Реализована технология REST API CRUD для основных моделей проекта, для аутентификации примненяются JWT-токены. В проекте реализованы пермишены, фильтрация, сортировка и поиск по запросам клиентов, реализована пагинация ответов от API, установлено ограничение количества запросов к API.

## Стек технологий
Python;
Django;
Django Rest Framework;
Pytest;
Simple-JWT;

## Запуск проекта
Клонировать репозиторий и перейти в него в командной строке:
git clone https://github.com/Yuriy-Grishin/API_YaTube.git

cd API_YaTube
Cоздать и активировать виртуальное окружение:
python3 -m venv env

source env/bin/activate
Установить зависимости из файла requirements.txt:
python3 -m pip install --upgrade pip

pip install -r requirements.txt
Выполнить миграции:
cd yatube_api

python3 manage.py migrate
Запустить проект (в режиме сервера Django):
python3 manage.py runserver
