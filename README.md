## Проект «API для Yatube»
**1. Описание проекта**
Благодаря этому проекту можно создавать посты, оставлять комментарии под постами и подписываться на понравившихся авторов.

**2. Технологии**
Python, Django, DRF, DRF-simplejwt

**3. Запуск проекта в dev-режиме**
Клонировать репозиторий и перейти в него в командной строке:
Установите и активируйте виртуальное окружение:
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip

Установите зависимости из файла requirements.txt
pip install -r requirements.txt

Перейдите в каталог с файлом manage.py выполните миграции:
python manage.py migrate

Создайте супер-пользователя:
python manage.py createsuperuser

Запуск проекта:
python manage.py runserver

**4. Примеры**
По умолчанию для неавторизованных пользователей проект доступен только для чтения.

api/v1/posts/ - получение списка всех постов
api/v1/posts/{id}/ - получение поста
api/v1/groups/ - получение списка всех групп
api/v1/groups/{id}/ - получение группы
api/v1/{post_id}/comments/ - получение списка всех комментариев под определенным постом
api/v1/{post_id}/comments/{id}/ - получение комментария
За исключением эндпоинта follow доступен только авторизованных пользователей.

api/v1/follow/ - получение подписок текущего пользователя
api/v1/follow/{id}/ - получение одной подписки
И users доступен только для админа:

api/v1/users/ - получение списка пользователей
api/v1/users/{id}/ - получение пользователя
Авторизованные пользователи могут создавать посты, комментировать их и подписываться на других пользователей.
Пользователи могут изменять(удалять) контент, автором которого они являются. Так же в проекте присутсвует пагинация(LimitOffsetPagination), поиск и сортировка

