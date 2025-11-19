"""Modulo simple con funciones aritméticas para demostrar CI/CD.

Incluye operaciones básicas y validaciones mínimas.
"""
from typing import Iterable


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def mean(values: Iterable[float]) -> float:
    """Calcula la media aritmética
    Lanza ValueError si la colección está vacía.
    """
    vals = list(values)
    if not vals:
        raise ValueError("values no puede estar vacío")
    return sum(vals) / len(vals)
