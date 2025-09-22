import argparse
from collections.abc import Callable
from reports.students_performance import performance_report

REPORTS: dict[str, Callable[[list[str]], None]] = {
    "students-performance": lambda files: performance_report(files, "student_name"),
}


def parse_args() -> argparse.Namespace:
    """Создает и парсит аргументы командной строки для генератора отчетов"""
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Генератор отчетов")
    parser.add_argument("--files", nargs="+", required=True, help="Список CSV файлов")
    parser.add_argument("--report", required=True, help="Название отчета")
    return parser.parse_args()

def main() -> None:
    """Главная функция программы"""
    args: argparse.Namespace = parse_args()
    try:
        REPORTS[args.report](args.files)
    except Exception as error:
        print(f"Произошла ошибка во время создания отчета {args.report}. Текст ошибки - {error}")

if __name__ == "__main__":
    main()