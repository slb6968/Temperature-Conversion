#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program ccontains functions for temperature conversions."""


import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Converts from Fahrenheit to Celsius.

    Args:
        degrees: Fahrenheit temperature in decimal value

    Returns:
        A temperature in Celsius equivalent to the input Fahrenheit degrees.

    Raises:
        NameError: name 'x' is not defined (argument must be a number)
    """
    return ((decimal.Decimal(degrees) - 32) * 5) / 9


def celsius_to_kelvin(degrees):
    """Converts from Celsius to Kelvin.

    Args:
        degrees: Celsius temperature in decimal value

    Returns:
        A temperature in Kelvin equivalent to the input Celsius degrees.

    Raises:
        NameError: name 'x' is not defined (argument must be a number)
    """
    return decimal.Decimal(degrees) + ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):
    """Converts from Fahrenheit to Kelvin by first converting from Fahrenheit
    to Celsius.

    Args:
        degrees: Fahrenheit temperature in decimal value

    Returns:
        A temperature in Kelvin equivalent to the input Fahrenheit degrees.

    Raises:
        NameError: name 'x' is not defined (argument must be a number)
    """
    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))
