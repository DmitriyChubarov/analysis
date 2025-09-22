import pytest
from analysis_project.main import parse_args, REPORTS, main

def test_parse_args(monkeypatch) -> None:
    """Проверяется, что parse_args возвращает правильные значения полей 'files' и 'report'"""
    monkeypatch.setattr("sys.argv", ["main.py",
                                     "--files", "file1.csv", "file2.csv",
                                     "--report", "students-performance"
                                     ])
    args = parse_args()
    assert args.report == "students-performance"
    assert args.files == ["file1.csv", "file2.csv"]

def test_parse_args_none(monkeypatch) -> None:
    """Проверяется, что parse_args возвращает ошибку при отсутствии 'files' и 'report'"""
    monkeypatch.setattr("sys.argv", ["main.py",
                                     ])
    with pytest.raises(SystemExit):
        parse_args()


def test_main_error(monkeypatch, capsys) -> None:
    """Проверяет обработку ошибки внутри main при генерации отчета"""
    def fake_report(files:list[str]) -> None:
        raise ValueError("Тестовая ошибка")

    monkeypatch.setitem(REPORTS, "students-performance", fake_report)
    monkeypatch.setattr("sys.argv", [
        "main.py",
        "--files", "file1.csv", "file2.csv",
        "--report", "students-performance"
    ])

    main()
    out = capsys.readouterr()
    assert "Произошла ошибка во время создания отчета students-performance. Текст ошибки - Тестовая ошибка" in out.out