# Docker

## Devepolment

### Run App

```
$ docker-compose -f docker-compose.yml -f docker-compose.dev.yml -p cms_dev up -d
$ docker exec -it cms_dev_web_1 python manage.py migrate
```

load test data

```
docker exec -it cms_dev_web_1 python manage.py loaddata test_data.json
```

### Clear

```
$ docker-compose -p cms_dev down
```

## Testing

### Run Test

```
$ docker-compose -f docker-compose.yml -f docker-compose.test.yml -p cms_test up -d
$ docker exec -it cms_test_web_1 pytest
```

Run with coverage report

```
$ docker exec -it cms_test_web_1 coverage run -m pytest
$ docker exec -it cms_test_web_1 coverage report
$ docker exec -it cms_test_web_1 coverage html
```

### Clear

```
$ docker-compose -p cms_test down
```
