# itmo-python-backend-course

## Run application

```
docker-compose up
```

## Run code checkers
```
docker exec -it itmo-python-backend-course-experiment_manager_demo-1 make format
```

```
docker exec -it itmo-python-backend-course-experiment_manager_demo-1 make lint
```

## Run Tests
```
docker exec -it itmo-python-backend-course-experiment_manager_demo-1 pytest
```
Unit tests dir: app/tests/unit
Integration tests dir: app/tests/integration