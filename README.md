## Шаги для запуска:
1) Собрать конфигурацию командой:
```shell
docker-compose -f docker-compose.prod.yml up -d --build
```
2) Отправить любой из [достуных запросов](https://github.com/wolf24ru/Dockers_HW/blob/Docker_1_ex_2/Django_project/requests-examples.http) на http://0.0.0.0:13337/api/v1

 

### Если не работает можно попробовать создать миграции вручную
```shell
docker-compose -f docker-compose.prod.yml exec django_app python manage.py migrate --noinput
```
