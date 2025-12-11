
name: Run Unit Tests

# События, которые запускают workflow
# - push: при любом коммите в любую ветку
# - pull_request: при создании или обновлении pull request
on: [push, pull_request]

# Определение задания (job) с именем "test"
jobs:
  test:
    # Стратегия выполнения с использованием матрицы
    # Позволяет запускать одни и те же тесты в разных средах
    strategy:
      matrix:
        # Матрица операционных систем
        # Согласно заданию: тесты выполняются на Ubuntu и Windows
        os: [ubuntu-latest, windows-latest]
    
    # Выбор runner'а из матрицы операционных систем
    # Для каждой OS в матрице создается отдельный запуск
    runs-on: ${{ matrix.os }}
    
    # Последовательность шагов для выполнения
    steps:
    # Шаг 1: Получение кода репозитория
    # Использует официальное действие checkout версии 3
    - uses: actions/checkout@v3
    
    # Шаг 2: Настройка Python окружения
    # Устанавливает Python на runner'е
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        # Указываем версию Python
        # '3.x' означает последнюю стабильную версию Python 3
        python-version: '3.x'
    
    # Шаг 3: Запуск unit-тестов
    - name: Run tests
      # Выполнение shell команд
      run: |
        # Переход в директорию с тестами
        cd geometric_lib
        
        # Запуск unit-тестов с помощью unittest
        # -m unittest: запуск модуля unittest
        # discover: автоматическое обнаружение тестовых файлов
        # -v: verbose режим (подробный вывод)
        python -m unittest discover -v