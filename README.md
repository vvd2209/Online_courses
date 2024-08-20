
# Тестовое задание Django/Backend

### О проекте
Проект представляет собой площадку для размещения онлайн-курсов с набором уроков. Доступ к урокам предоставляется после покупки курса (подписки). Внутри курса студенты автоматически распределяются по группам. У каждого пользователя есть баланс с бонусами.

### Для работы с проектом необходимо выполнить следующие действия:
- Клонировать репозиторий
- Активировать виртуальное окружение
- Установить зависимости pip install -r requirements.txt
- Перейти в папку product и применить миграции python manage.py migrate
- Создать суперпользователя командой python manage.py createsuperuser
- Заупстить сервер командой python manage.py runserver
- Откройте браузер и перейдите по адресу http://127.0.0.1:8000 для доступа к приложению

### __OpenAPI документация__
* Swagger: http://127.0.0.1:8000/api/v1/swagger/
* ReDoc: http://127.0.0.1:8000/api/v1/redoc/

### __Технологии__
* [Python 3.10.12](https://www.python.org/doc/)
* [Django 4.2.10](https://docs.djangoproject.com/en/4.2/)
* [Django REST Framework  3.14.0](https://www.django-rest-framework.org/)
* [Djoser  2.2.0](https://djoser.readthedocs.io/en/latest/getting_started.html)
