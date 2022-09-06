# test_task_inside

Выполнение тестового задания на позицию junior разработчика

После клонирования проекта из репозитория.
Команда `docker-compose up --build` Создаст и запустит контейнеры
В браузере проверяем запущенный проект http://127.0.0.1:5050/v1/docs#/

Доступ к БД 

Хост: localhost

имя БД: test_task_inside

Пользователь: fastapi

Пароль: fastapi

Проект на FastAPI

БД PostgreSQL

ОРМ SQLAlchemy.orm

Миграции библиотека alembic

Реляции выполнены на уровне моделей SQLAlchemy т.к. используем ОРМ.

JWT реализован на библиотеке PyJWT

В токене хранится имя пользователя и время создания токена

Время "жизни" токена 5 минут.


CURL:
>Создание пользователя

curl -X 'POST' \
  'http://127.0.0.1:5050/v1/signup' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Катя",
  "password": "Катя"
}'

Получаем ответ:
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiXHUwNDFhXHUwNDMwXHUwNDQyXHUwNDRmIiwiaWF0IjoxNjYyNDUzODgxfQ.xH6AK_3XALOu4UnaxqWgswo2d0LpM6WDE0Sw7MOLfrU"
}

>Авторизация  пользователя по имени и паролю

curl -X 'POST' \
  'http://127.0.0.1:5050/v1/users/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=&username=%D0%9A%D0%B0%D1%82%D1%8F&password=%D0%9A%D0%B0%D1%82%D1%8F&scope=&client_id=&client_secret='

  Ответ
  	
Response body
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiXHUwNDFhXHUwNDMwXHUwNDQyXHUwNDRmIiwiaWF0IjoxNjYyNDU0NTI3fQ.ugFJBOqnBOtttkKGvqQkowKcg8t_0JykqD8PaRkQpIE"
}


>Создание сообщения

curl -X 'POST' \
  'http://127.0.0.1:5050/v1/messages/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer Bearer_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiXHUwNDFhXHUwNDMwXHUwNDQyXHUwNDRmIiwiaWF0IjoxNjYyNDUzODgxfQ.xH6AK_3XALOu4UnaxqWgswo2d0LpM6WDE0Sw7MOLfrU' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Катя",
  "message": "Привет"
}'

>Получение сообщений

curl -X 'POST' \
  'http://127.0.0.1:5050/v1/messages/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer Bearer_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiXHUwNDFhXHUwNDMwXHUwNDQyXHUwNDRmIiwiaWF0IjoxNjYyNDUzODgxfQ.xH6AK_3XALOu4UnaxqWgswo2d0LpM6WDE0Sw7MOLfrU' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Катя",
  "message": "history 5"
}'



