# Анализ успеваемости студентов

- Пример запуска скрипта(```python3 main.py --files students1.csv students2.csv --report students-performance```):
<img width="1005" height="396" alt="image" src="https://github.com/user-attachments/assets/4ee0d3f1-174a-4b67-b54b-303f4e328134" />

- Покрытие тестами(```PYTHONPATH=. pytest --cov(в таком формате запуск из корня)```):
<img width="1005" height="340" alt="image" src="https://github.com/user-attachments/assets/df7c1148-52fa-4ddd-9c72-9bba9584289f" />

- Масштабирование: чтобы добавить отчет с сортировкой по другому полю, необходимо в словарь REPORTS в файле main.py добавить новую строку с указанием нужного поля
```bash
REPORTS: dict[str, Callable[[list[str]], None]] = {
    "students-performance": lambda files: performance_report(files, "student_name"),
    "students-performance": lambda files: performance_report(files, "teacher_name"), #пример
}
```
- Если логика нового отчета будет кардинально отличаться, создаем функцию для его формирования и добавляем строку в REPORTS

### Контакты
- tg: @eeezz_z
- gh: https://github.com/DmitriyChubarov
