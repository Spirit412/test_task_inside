FROM python:3.10

COPY ./alembic /test_task_inside/alembic
COPY ./api /test_task_inside/api
COPY ./requirements.txt /test_task_inside
COPY ./alembic.ini /test_task_inside

RUN pip3 install -r /test_task_inside/requirements.txt

EXPOSE 5050