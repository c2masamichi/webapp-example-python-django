# Docker

## Devepolment

### Build

```
$ docker-compose -p django_cms build
```

### Run App

```
$ docker-compose -p django_cms up -d
$ docker exec -it django_cms_app_1 python manage.py migrate
```

create superuser

```
$ docker exec -it django_cms_app_1 python manage.py createsuperuser --username dev-user --email dev-user@example.com
```

load test data

```
$ docker exec -it django_cms_app_1 python manage.py loaddata test_data.json
```

### Run Test

```
$ docker-compose -p django_cms up -d
$ cd app/
$ docker exec -it django_cms_app_1 pytest
```

Run with coverage report

```
$ docker exec -it django_cms_app_1 coverage run -m pytest
$ docker exec -it django_cms_app_1 coverage report
$ docker exec -it django_cms_app_1 coverage html
```

### Clear

```
$ docker-compose -p django_cms down
```
