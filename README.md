Агентство недвижимости
Это приложение предназначено для управления агентством недвижимости. Оно позволяет вести учет квартир, клиентов и менеджеров, а также отслеживать статусы объектов недвижимости.

Основные модели данных
Category (Категория)
Представляет категорию объекта недвижимости.
Поля:
title: Имя объекта (CharField, max_length=32).
Status (Статус)
Представляет статус объекта недвижимости.
Поля:
title: Название статуса (CharField, max_length=16).
description: Описание статуса (TextField).
Clients (Клиенты)
Представляет клиентов агентства недвижимости.
Поля:
bio: ФИО клиента (CharField, max_length=128).
number_phone: Номер телефона (SmallIntegerField).
contract: Номер договора (SmallIntegerField).
status: Связь с моделью Status (ForeignKey).
Flats (Квартиры)
Представляет квартиры, которыми управляет агентство недвижимости.
Поля:
apartment_number: Номер квартиры (CharField, max_length=16).
object: Связь с моделью Category (ForeignKey).
floor: Этаж (SmallIntegerField, default=1).
square: Площадь квартиры (DecimalField, default=144.5, decimal_places=1, max_digits=4).
create_date: Дата создания (DateTimeField, auto_now=True).
status: Связь с моделью Status (ForeignKey).
price: Цена (PositiveIntegerField, default=2000000).
Manager (Менеджер)
Представляет менеджеров агентства недвижимости.
Поля:
bio: ФИО менеджера (CharField, max_length=128).
number_phone: Номер телефона (SmallIntegerField).
email: Почта (EmailField).
create_date: Дата создания (DateTimeField, auto_now=True).
count: Количество сделок (SmallIntegerField, default=0).
password: Временный пароль (CharField, max_length=32).
Установка и использование
Клонируйте репозиторий на ваш компьютер.
Установите необходимые зависимости с помощью команды pip install -r requirements.txt.
Запустите сервер разработки с помощью команды python manage.py runserver.
Откройте браузер и перейдите по адресу http://127.0.0.1:8000/ для доступа к приложению.


Автор
Джаманкулов Эрлан

