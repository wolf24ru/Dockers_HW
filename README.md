## Шаги для запуска:
1) Создать из Dokerfile образ (имя тега может быть другим):
```shell
docker build --tag django_project:1.0 ./
```
2) Запустить Docker контейнер (порт cлева может быть любым другим доступным портом):
```shell
docker run -p 8000:8000 -d --name django_server django_project:1.0
```
3) Отправить любой из [достуных запросов](https://github.com/wolf24ru/Dockers_HW/blob/Docker_1_ex_2/Django_project/requests-examples.http) на http://0.0.0.0:8000/api/v1
