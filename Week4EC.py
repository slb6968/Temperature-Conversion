#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program ccontains functions for temperature conversions."""


import decimal
import task_01

# Three Conversion Functions similar to those in the Synthesizing Tasks


def celsius_to_fahrenheit(degrees):
    """Converts from Celsius to Fahrenheit.

    Args:
        degrees: Celsius temperature

    Returns:
        A temperature in Fahrenheit equivalent to the input Celsius decimal.

    Raises:
        NameError: name 'x' is not defined (argument must be a number)
    """
    return decimal.Decimal(degrees) * 9 / 5 + 32


def kelvin_to_celsius(degrees):
    """Converts from Kelvin to Celsius.

    Args:
        degrees: Kelvin temperature in decimal value

    Returns:
        A temperature in Celsius equivalent to the input Kelvin degrees.

    Raises:
        NameError: name 'x' is not defined (argument must be a number)
    """
    return decimal.Decimal(degrees) - task_01.ABSOLUTE_DIFFERENCE


def kelvin_to_fahrenheit(degrees):
    """Converts from Kelvin to Fahrenheit by first converting from Kelvin
    to Celsius.

    Args:
        degrees: Kelvin temperature in decimal value

    Returns:
        A temperature in Fahrenheit equivalent to the input Kelvin degrees.

    Raises:
        NameError: name 'x' is not defined (argument must be a number)
    """
    return celsius_to_fahrenheit(kelvin_to_celsius(degrees))

# A conversion function for any temperature


def temp_convert(temperature):
    """Converts from Kelvin to Fahrenheit by first converting from Kelvin
    to Celsius.

    Args:
        temperature: any decimal-valued Celsius/Kelvin/Fahrenheit temperature

    Returns:
        Prints the entered temperature and its equivalent temperature in
        Kelvin, Celsius and Fahrenheit degrees rounded to two digits.
        For example temp_convert(0) provides the following output:
            0 degrees Fahrenheit = -17.78 degrees Celsius or 255.37 Kelvin
            0 degrees Celsius = 32.0 degrees Fahrenheit or 273.15 Kelvin
            0 Kelvin = -273.15 degrees Celsius or -459.67 degrees Fahrenheit
    """

    tempstr = (str(temperature) + ' {0} = {1} {2} or {3} {4}')
    celsius = (decimal.Decimal(temperature) - 32) * 5 / 9
    kelvin = celsius + task_01.ABSOLUTE_DIFFERENCE
    print tempstr.format('degrees Fahrenheit', round(celsius, 2),
                         'degrees Celsius', round(kelvin, 2), 'Kelvin')
    fahrenheit = decimal.Decimal(temperature) * 9 / 5 + 32
    kelvin = decimal.Decimal(temperature) + task_01.ABSOLUTE_DIFFERENCE
    print tempstr.format('degrees Celsius', round(fahrenheit, 2),
                         'degrees Fahrenheit', round(kelvin, 2), 'Kelvin')
    celsius = decimal.Decimal(temperature) - task_01.ABSOLUTE_DIFFERENCE
    fahrenheit = celsius * 9 / 5 + 32
    print tempstr.format('Kelvin', round(celsius, 2), 'degrees Celsius',
                         round(fahrenheit, 2), 'degrees Fahrenheit')
    return
