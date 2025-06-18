"""Utilities for converting between Celsius and Fahrenheit."""

from __future__ import annotations


def celsius_to_fahrenheit(celsius: float) -> tuple[float, float]:
    """Convert Celsius to Fahrenheit.

    Returns a tuple containing the original Celsius value and the
    corresponding Fahrenheit value.
    """
    fahrenheit = celsius * 9 / 5 + 32
    return celsius, fahrenheit


def fahrenheit_to_celsius(fahrenheit: float) -> tuple[float, float]:
    """Convert Fahrenheit to Celsius.

    Returns a tuple containing the original Fahrenheit value and the
    corresponding Celsius value.
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return fahrenheit, celsius


if __name__ == "__main__":
    # Example usage showing both conversions
    example_celsius = 0.0
    example_fahrenheit = 32.0
    print(f"{example_celsius}°C -> {celsius_to_fahrenheit(example_celsius)[1]}°F")
    print(f"{example_fahrenheit}°F -> {fahrenheit_to_celsius(example_fahrenheit)[1]}°C")
