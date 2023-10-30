# test_QL

## Test Task
*Ссылка на страницу Text Box: https://demoqa.com/text-box*
*Форма: Text Box*
### *Задание:*
*Написать фреймворк для тестирования этой формы с использованием шаблон проектирования PageObject.*
### *Короткий план:*
+ *Заполнить все поля рандомными данными (можно использовать дополнительные библиотеки).*
+ *Нажать кнопку Submit*
+ *Сравнить введенные данные с полученными данными из поля в котором будут все заполненные данные.*

*Фреймворк закинуть в репозиторий и дать ссылку.*
*Примерное время выполнения 1-2 часа.*

## Instalation
Clone repository from github. 
Create venv: ```python3 -m venv venv```
Activate venv: ```venv/bin/activate```
Install all required dependencies from *requirements.txt*: ```pip3 install -r requirements.txt```

## Run test and view report
Run test: ```python3 -m pytest --alluredir \report```

View report: ```allure serve report```