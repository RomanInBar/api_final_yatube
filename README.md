# API. Финальный проект.
## Описание
#### Предоставляет доступ к функционалу, без посещения сайта.
#### Функционал:
* Подписка на пользователя.
* Создавать, просматривать, изменять, удалять посты.
* Просматривать, создавать группы.
* Создавать, просматривать, изменять, удалять комменатрии.
* Совершать поиск по подпискам. 

#### Документация к API : `http://localhost:8000/redoc/`

## Установка
Клонировать репозиторий и перейти в него в командной строке:
```
https://github.com/RomanInBar/api_final_yatube.git

cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env

source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Реализация

___Примечание: доступ на чтение доступно всем пользователям___
___(ко всему, кроме подписок пользователя)___.

Для доступа ко всему функционалу API необходимо получить токен.
Нужно выполнить POST запрос на `/api/v1/token`, передав `username` и `password`___(активный аккаунт)___. API вернёт JWT-токен.

POST запрос на получение токена. (VSCode):
```
POST http://127.0.0.1:8000/api/v1/token
Content-Type: application/json

{
    "username": "Username",
    "password": "password"
}
```

Дальше, передав токен, можно будет обращаться к методам, например:
`(GET, POST, PATCH, PUT, DELETE) https://localhost/api/v1/posts/`

При отправке запроса, не забывайте передавать токен:
`Authorization: Bearer <токен>`

POST запрос на создание поста. (VSCode)
```
POST http://127.0.0.1:8000/api/v1/posts/
Authorization: Bearer <ваш токен>
Content-Type: application/json

{
    "text": "string"
}
```

