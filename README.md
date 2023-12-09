Каталог марок и моделей автомобилей с auto.ru. Проект использует БД SQLite.

## Установка
```bash
 python3 -m venv venv
 venv/bin/pip install -r requirements.txt 
```

## Запуск сервера
```
cd myproject/
../venv/bin/python manage.py runserver
```

## Обновить каталог
Каталог обновляется командой `update_autoru_catalog`
```bash
cd myproject/
../venv/bin/python manage.py update_autoru_catalog
```

Команда собирает с каталога auto.ru марки и модели автомобилей и заносит их в базу данных. В базе данных 2 модели: __*Марка и Модель.*__. У Модели внешний ключ на Марку.

![Схема моделей](https://github.com/ralbakov/git_adv/blob/main/docs/models.png?raw=true)

При каждом вызове *update_autoru_catalog* удаляюся прошлые данные из базы и загружаются новые. Значение марки берется из атрибута name, тега mark, например из: `<mark name="Thairung">` берется _Thairung_. Значение модели берется из атрибута name, тега folder, до запятой. Например из: `<folder name="Transformer, II" id="23666273">``` берется _Transformer._. Марок примерно 350, моделей свыше 3500.