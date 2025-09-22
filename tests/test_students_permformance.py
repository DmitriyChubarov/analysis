from analysis_project.reports.students_performance import performance_report

def test_students_performance_report(capsys, tmp_path) -> None:
    """Проверяется, что students_performance_report возвращает правильные данные"""
    csv = tmp_path / "test.csv"
    csv.write_text("student_name,grade\nЕкатерина,5\nЕкатерина,3\n", encoding="utf-8")

    performance_report([str(csv)], 'student_name')

    out = capsys.readouterr()
    assert "Екатерина" in out.out
    assert "4" in out.out

def test_students_performance_report_column(capsys, tmp_path) -> None:
    """Проверяется, что students_performance_report возвращает ошибку при отсутствии 'student_name' и 'grade'"""
    csv = tmp_path / "test.csv"
    csv.write_text("\nЕкатерина,5\nЕкатерина,3\n", encoding="utf-8")

    performance_report([str(csv)], 'student_name')

    out = capsys.readouterr()
    assert "должен содержать столбцы" in out.out

def test_students_performance_report_score(capsys, tmp_path) -> None:
    """Проверяется корректность введенных оценок в csv"""
    csv = tmp_path / "test.csv"
    csv.write_text("student_name,grade\nЕкатерина,пять\nЕкатерина,три\n", encoding="utf-8")

    performance_report([str(csv)], 'student_name')

    out = capsys.readouterr()
    assert "Некорректная оценка для студента" in out.out

def test_students_performance_report_file(capsys, tmp_path) -> None:
    """Проверяется, что students_performance_report возвращает ошибку при отсутствии csv файла"""
    performance_report(["scv_fake.csv"], 'student_name')

    out = capsys.readouterr()
    assert "Файл scv_fake.csv не найден" in out.out
    assert "Нет данных для отображения" in out.out