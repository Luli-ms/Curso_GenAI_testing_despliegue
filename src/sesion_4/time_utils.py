# src/time_utils.py

from datetime import datetime, timedelta

def calculate_duration(start: str, end: str) -> int:
    """
    Calcula la duración en minutos entre dos horas en formato HH:MM.
    Si la hora de fin es menor a la de inicio, se asume que es del día siguiente.
    """
    fmt = "%H:%M"
    try:
        start_dt = datetime.strptime(start, fmt)
        end_dt = datetime.strptime(end, fmt)
    except ValueError:
        return -1

    # Si la hora final es anterior a la inicial, sumamos un día (24 horas)
    if end_dt < start_dt:
        end_dt += timedelta(days=1)

    delta = end_dt - start_dt
    return int(delta.total_seconds() / 60)


def is_valid_shift(start: str, end: str) -> bool:
    """
    Un turno es válido si dura entre 30 minutos y 8 horas
    """
    duration = calculate_duration(start, end)
    return 30 <= duration <= 480


if __name__ == "__main__":
    print(calculate_duration("abc", "pepe"))
    print(is_valid_shift("23:30", "00:15"))