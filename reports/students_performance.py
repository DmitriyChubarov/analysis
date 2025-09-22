import csv
from tabulate import tabulate


def performance_report(files: list[str], field: str) -> None:
    """Генерирует отчет средних оценок"""
    grades: dict[str, list[float]] = {}

    for file in files:
        try:    
            with open(file, newline="", encoding="utf-8") as f:
                reader: csv.DictReader = csv.DictReader(f)
                if field not in reader.fieldnames or 'grade' not in reader.fieldnames:
                    raise ValueError(f"Файл {f} должен содержать столбцы {field} и 'grade'.")
                for row in reader:
                    x: str = row[field]
                    try:
                        grade:float = float(row["grade"])
                    except ValueError:
                        print(f"Некорректная оценка для студента {x}")
                        continue
                    if x not in grades:
                        grades[x] = []
                    grades[x].append(grade)

        except FileNotFoundError:
            print(f'Файл {file} не найден')
        except Exception as error:
            print(f'Ошибка чтения файла - {error}')
    
    data: list[tuple[str, float]] = [
        (obj, round(sum(scores) / len(scores), 1)) for obj, scores in grades.items()
    ]

    data.sort(key=lambda x: x[1], reverse=True)
    
    if data:
        print(tabulate(data, headers=[field, "grade"], showindex=1, floatfmt=".1f"))
    else:
        print("Нет данных для отображения")