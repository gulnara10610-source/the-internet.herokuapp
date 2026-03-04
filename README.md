# QA Tests

Тестовое окружение для автоматизированного тестирования с использованием Docker и Allure.

## Быстрый старт

### Сборка образа
```bash
docker build -t zentist-tests .
```

### Запуск тестов
```bash

docker run --rm \
  -e BASE_URL=https://the-internet.herokuapp.com
  -v $(pwd)/allure-results:/usr/src/app/allure-results \
  -v $(pwd)/allure-report:/usr/src/app/allure-report \
```

### Генерация отчета
```bash

allure generate allure-results --clean -o allure-report
```

### Просмотр отчета
```bash

allure open allure-report
```

## Параметры

- `-n 2` - параллельное выполнение в 2 потока
- `--reruns 2` - количество повторных попыток при неудаче
- `--reruns-delay 2` - задержка между попытками (секунды)
- `--alluredir=allure-results` - папка для результатов Allure

## Переменные окружения

- `BASE_URL` - URL основного приложения

