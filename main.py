import argparse

from reports.students_performance import students_performance_report

REPORTS = {
    "students-performance": students_performance_report,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Генератор отчетов")
    parser.add_argument("--files", nargs="+", required=True, help="Список CSV файлов")
    parser.add_argument("--report", required=True, help="Название отчета")
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    try:
        REPORTS[args.report](args.files)
    except Exception as error:
        print(f"Произошла ошибка во время создания отчета {args.report}. Тексто ошибки - {error}")

if __name__ == "__main__":
    main()