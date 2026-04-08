# src/time_utils.py

from datetime import datetime

def calculate_duration(start: str, end: str) -> int:
    """
    Calcula la duración en minutos entre dos horas en formato HH:MM
    """
    fmt = "%H:%M"
    start_dt = datetime.strptime(start, fmt)
    end_dt = datetime.strptime(end, fmt)

    delta = end_dt - start_dt
    return int(delta.total_seconds() / 60)


def is_valid_shift(start: str, end: str) -> bool:
    """
    Un turno es válido si dura entre 30 minutos y 8 horas
    """
    duration = calculate_duration(start, end)
    return 30 <= duration <= 480