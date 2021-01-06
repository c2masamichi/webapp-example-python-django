# Docker

## Devepolment

### Run App

```
$ docker-compose -f docker-compose.yml -f docker-compose.dev.yml -p django_webapi_dev up -d
$ docker exec -it django_webapi_dev_web_1 python manage.py migrate
```

load test data

```
docker exec -it django_webapi_dev_web_1 python manage.py loaddata test_data.json
```

### Clear

```
$ docker-compose -p django_webapi_dev down
```

## Testing

### Run Test

```
$ docker-compose -f docker-compose.yml -f docker-compose.test.yml -p django_webapi_test up -d
$ docker exec -it django_webapi_test_web_1 pytest
```

Run with coverage report

```
$ docker exec -it django_webapi_test_web_1 coverage run -m pytest
$ docker exec -it django_webapi_test_web_1 coverage report
$ docker exec -it django_webapi_test_web_1 coverage html
```

### Clear

```
$ docker-compose -p django_webapi_test down
```
