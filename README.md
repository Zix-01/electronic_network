# Веб-приложение для сети по продаже электроники

Это веб-приложение разработано с использованием Django и Django REST Framework (DRF) для управления иерархической структурой сети по продаже электроники. Приложение включает в себя админ-панель и API для работы с данными о заводах, розничных сетях и индивидуальных предпринимателях.

## Технические требования

- Python 3.8+
- Django 3+
- Django REST Framework 3.10+
- PostgreSQL 10+

## Установка

### Клонирование репозитория

bash
git clone https://github.com/electronic_network
cd electronic_network

### Создание виртуального окружения

bash
python -m venv venv
source venv/bin/activate  # Для Windows используйте venvScriptsactivate

### Установка зависимостей

bash
pip install -r requirements.txt

### Применение миграций

bash
python manage.py migrate

### Запуск сервера

bash
python manage.py runserver

Теперь ваше приложение доступно по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Использование

### Админ-панель

Вы можете получить доступ к админ-панели по адресу [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin). Для входа используйте учетные данные суперпользователя, которые можно создать с помощью команды:

bash
python manage.py createsuperuser
  
#### Доступ к API

Только активные сотрудники имеют доступ к API.
