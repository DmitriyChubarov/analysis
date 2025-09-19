import csv
import sys
from tabulate import tabulate
from typing import Sequence


def students_performance_report(files: Sequence[str]) -> None:
    grades: dict[str, list[float]] = {}

    for file in files:
        try:    
            with open(file, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                if 'student_name' not in reader.fieldnames or 'grade' not in reader.fieldnames:
                    raise ValueError(f"Файл {f} должен содержать столбцы 'student_name' и 'grade'.")
                for row in reader:
                    student: str = row["student_name"]
                    try:
                        grade = float(row["grade"])
                    except ValueError:
                        print(f"Некорректная оценка для студента {student}")
                        continue
                    if student not in grades:
                        grades[student] = []
                    grades[student].append(grade)

        except FileNotFoundError:
            print(f'Файл {file} не найден')
        except Exception as error:
            print(f'Ошибка чтения файла - {error}')
    
    data: list[tuple[str, float]] = [
        (student, round(sum(scores) / len(scores), 1)) for student, scores in grades.items()
    ]

    data.sort(key=lambda x: x[1], reverse=True)
    
    if data:
        print(tabulate(data, headers=["student_name", "grade"], showindex=1))
    else:
        print("Нет данных для отображения")