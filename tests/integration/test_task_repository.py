from pathlib import Path
import sys
from uuid import uuid4

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from sesion_4.task_repository import (
    add_task,
    get_all_tasks,
    get_tasks_by_status,
    init_db,
)


@pytest.fixture
def temp_db_path() -> Path:
    # Arrange
    temp_dir = Path(__file__).resolve().parents[1] / ".tmp"
    temp_dir.mkdir(exist_ok=True)
    db_path = temp_dir / f"{uuid4().hex}.sqlite"
    init_db(db_path=str(db_path))
    yield db_path

    if db_path.exists():
        db_path.unlink()


@pytest.fixture
def valid_statuses() -> tuple[str, ...]:
    return ("pending", "in_progress", "done")


def test_init_db_creates_a_usable_empty_database(temp_db_path: Path) -> None:
    # Arrange

    # Act
    tasks = get_all_tasks(db_path=str(temp_db_path))

    # Assert
    assert temp_db_path.exists()
    assert tasks == []


@pytest.mark.parametrize(
    ("title", "status"),
    [
        ("Preparar laboratorio", "pending"),
        ("Corregir ejercicios", "done"),
        ("Revisar entregas", "in_progress"),
    ],
)
def test_add_task_persists_rows_in_sqlite_database(
    temp_db_path: Path, title: str, status: str
) -> None:
    # Arrange

    # Act
    add_task(title=title, status=status, db_path=str(temp_db_path))
    tasks = get_all_tasks(db_path=str(temp_db_path))

    # Assert
    assert len(tasks) == 1
    assert tasks[0][1:] == (title, status)


def test_get_all_tasks_returns_inserted_rows_in_insertion_order(
    temp_db_path: Path,
) -> None:
    # Arrange
    add_task(title="Tarea 1", status="pending", db_path=str(temp_db_path))
    add_task(title="Tarea 2", status="done", db_path=str(temp_db_path))

    # Act
    tasks = get_all_tasks(db_path=str(temp_db_path))

    # Assert
    assert len(tasks) == 2
    assert tasks[0][1:] == ("Tarea 1", "pending")
    assert tasks[1][1:] == ("Tarea 2", "done")
    assert tasks[0][0] < tasks[1][0]


@pytest.mark.parametrize(
    ("selected_status", "expected_titles"),
    [
        ("pending", ["Tarea A", "Tarea C"]),
        ("done", ["Tarea B"]),
        ("blocked", []),
    ],
)
def test_get_tasks_by_status_returns_only_matching_rows(
    temp_db_path: Path, selected_status: str, expected_titles: list[str]
) -> None:
    # Arrange
    add_task(title="Tarea A", status="pending", db_path=str(temp_db_path))
    add_task(title="Tarea B", status="done", db_path=str(temp_db_path))
    add_task(title="Tarea C", status="pending", db_path=str(temp_db_path))

    # Act
    tasks = get_tasks_by_status(selected_status, db_path=str(temp_db_path))

    # Assert
    assert [task[1] for task in tasks] == expected_titles
    assert all(task[2] == selected_status for task in tasks)


@pytest.mark.parametrize("empty_title", ["", " ", "   "])
def test_add_task_rejects_empty_titles(
    temp_db_path: Path, empty_title: str
) -> None:
    # Arrange

    # Act / Assert
    with pytest.raises(ValueError):
        add_task(title=empty_title, status="pending", db_path=str(temp_db_path))


@pytest.mark.parametrize("invalid_status", ["blocked", "archived", "", "DONE"])
def test_add_task_rejects_invalid_status_values(
    temp_db_path: Path, invalid_status: str
) -> None:
    # Arrange

    # Act / Assert
    with pytest.raises(ValueError):
        add_task(title="Tarea inválida", status=invalid_status, db_path=str(temp_db_path))


def test_get_tasks_by_status_does_not_return_rows_from_other_statuses(
    temp_db_path: Path,
) -> None:
    # Arrange
    add_task(title="Pendiente 1", status="pending", db_path=str(temp_db_path))
    add_task(title="Hecha 1", status="done", db_path=str(temp_db_path))
    add_task(title="En curso 1", status="in_progress", db_path=str(temp_db_path))
    add_task(title="Pendiente 2", status="pending", db_path=str(temp_db_path))

    # Act
    pending_tasks = get_tasks_by_status("pending", db_path=str(temp_db_path))

    # Assert
    assert [task[1] for task in pending_tasks] == ["Pendiente 1", "Pendiente 2"]
    assert [task[2] for task in pending_tasks] == ["pending", "pending"]


def test_temp_database_starts_empty_for_each_test_case(temp_db_path: Path) -> None:
    # Arrange

    # Act
    tasks = get_all_tasks(db_path=str(temp_db_path))

    # Assert
    assert tasks == []
