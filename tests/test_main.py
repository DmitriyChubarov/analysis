import pytest
from analysis_project.main import parse_args

def test_parse_args(monkeypatch):
    monkeypatch.setattr("sys.argv", [
        "main.py",
        "--files", "file1.csv", "file2.csv",
        "--report", "students-performance"
    ])
    args = parse_args()
    assert args.report == "students-performance"
    assert args.files == ["file1.csv", "file2.csv"]
