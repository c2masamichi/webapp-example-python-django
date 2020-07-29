# Docker

## Devepolment

### Run App

```
$ docker-compose -f docker-compose.yml -f docker-compose.dev.yml -p webapi_dev up -d
$ docker exec -it webapi_dev_web_1 python manage.py migrate
```

load test data

```
docker exec -it webapi_dev_web_1 python manage.py loaddata test_data.json
```

### Clear

```
$ docker-compose -p webapi_dev down
```

## Testing

### Run Test

```
$ docker-compose -f docker-compose.yml -f docker-compose.test.yml -p webapi_test up -d
$ docker exec -it webapi_test_web_1 pytest
```

Run with coverage report

```
$ docker exec -it webapi_test_web_1 coverage run -m pytest
$ docker exec -it webapi_test_web_1 coverage report
$ docker exec -it webapi_test_web_1 coverage html
```

### Clear

```
$ docker-compose -p webapi_test down
```
