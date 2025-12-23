"""
Basic compound interest calculations.
"""

import math


def future_value(principal: float, rate: float, time: float, 
                 compounding: int = 1) -> float:
    """
    Calculate the future value of an investment with compound interest.
    
    Formula: FV = P * (1 + r/n)^(n*t)
    
    Args:
        principal: Initial investment amount (P)
        rate: Annual interest rate (decimal, e.g., 0.05 for 5%)
        time: Time in years (t)
        compounding: Number of compounding periods per year (n)
    
    Returns:
        Future value of the investment
    
    Raises:
        ValueError: If any input is invalid
    
    Examples:
        >>> future_value(1000, 0.05, 10)
        1628.894626777442
        >>> future_value(1000, 0.05, 10, 12)
        1647.00949769028
    """
    # Проверка входных данных
    if principal < 0:
        raise ValueError("Principal cannot be negative")
    if rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if time < 0:
        raise ValueError("Time cannot be negative")
    if compounding <= 0:
        raise ValueError("Compounding periods must be positive")
    
    return principal * (1 + rate/compounding) ** (compounding * time)


def present_value(future_value_amount: float, rate: float, time: float, 
                  compounding: int = 1) -> float:
    """
    Calculate the present value needed to reach a future value.
    
    Formula: PV = FV / (1 + r/n)^(n*t)
    
    Args:
        future_value_amount: Desired future amount (FV)
        rate: Annual interest rate (decimal)
        time: Time in years
        compounding: Number of compounding periods per year
    
    Returns:
        Present value needed
    
    Raises:
        ValueError: If any input is invalid
    
    Examples:
        >>> present_value(1000, 0.05, 5)
        783.5261664684584
    """
    # Проверка входных данных
    if future_value_amount < 0:
        raise ValueError("Future value cannot be negative")
    if rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if time < 0:
        raise ValueError("Time cannot be negative")
    if compounding <= 0:
        raise ValueError("Compounding periods must be positive")
    
    return future_value_amount / (1 + rate/compounding) ** (compounding * time)


def compound_interest(principal: float, rate: float, time: float, 
                      compounding: int = 1) -> float:
    """
    Calculate the compound interest earned.
    
    Formula: CI = P * [(1 + r/n)^(n*t) - 1]
    
    Args:
        principal: Initial investment amount
        rate: Annual interest rate (decimal)
        time: Time in years
        compounding: Number of compounding periods per year
    
    Returns:
        Compound interest earned
    
    Raises:
        ValueError: If any input is invalid
    
    Examples:
        >>> compound_interest(1000, 0.05, 10)
        628.894626777442
    """
    # Проверка входных данных
    if principal < 0:
        raise ValueError("Principal cannot be negative")
    if rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if time < 0:
        raise ValueError("Time cannot be negative")
    if compounding <= 0:
        raise ValueError("Compounding periods must be positive")
    
    return principal * ((1 + rate/compounding) ** (compounding * time) - 1)


def annual_rate(present_value: float, future_value: float, time: float, 
                compounding: int = 1) -> float:
    """
    Calculate the annual interest rate needed.
    
    Formula: r = n * [(FV/PV)^(1/(n*t)) - 1]
    
    Args:
        present_value: Current value (PV)
        future_value: Desired future value (FV)
        time: Time in years
        compounding: Number of compounding periods per year
    
    Returns:
        Required annual interest rate (decimal)
    
    Raises:
        ValueError: If any input is invalid
    
    Examples:
        >>> annual_rate(1000, 2000, 10)
        0.07177346253629311  # ≈7.18%
    """
    # Проверка входных данных
    if present_value <= 0:
        raise ValueError("Present value must be positive")
    if future_value <= 0:
        raise ValueError("Future value must be positive")
    if future_value <= present_value:
        raise ValueError("Future value must be greater than present value")
    if time <= 0:
        raise ValueError("Time must be positive")
    if compounding <= 0:
        raise ValueError("Compounding periods must be positive")
    
    return compounding * ((future_value / present_value) ** (1 / (compounding * time)) - 1)


def time_to_goal(principal: float, future_value: float, rate: float, 
                 compounding: int = 1) -> float:
    """
    Calculate time needed to reach investment goal.
    
    Formula: t = log(FV/PV) / (n * log(1 + r/n))
    
    Args:
        principal: Initial investment
        future_value: Desired future value
        rate: Annual interest rate (decimal)
        compounding: Number of compounding periods per year
    
    Returns:
        Time in years
    
    Raises:
        ValueError: If any input is invalid
        ZeroDivisionError: If rate is zero
    
    Examples:
        >>> time_to_goal(1000, 2000, 0.07)
        10.244768351057632  # ≈10.25 years
    """
    # Проверка входных данных
    if principal <= 0:
        raise ValueError("Principal must be positive")
    if future_value <= 0:
        raise ValueError("Future value must be positive")
    if rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if compounding <= 0:
        raise ValueError("Compounding periods must be positive")
    
    if rate == 0:
        if future_value <= principal:
            raise ValueError("With zero interest, future value must be greater than principal")
        # При нулевой ставке: время = (будущее - настоящее) / 0 - не определено
        raise ValueError("Cannot calculate time with zero interest rate")
    
    if future_value <= principal:
        raise ValueError("Future value must be greater than principal")
    
    return math.log(future_value / principal) / (compounding * math.log(1 + rate/compounding))