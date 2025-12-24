import math


def future_value(principal: float, rate: float, time: float, #Расчет будущей стоимости
                 compounding: int = 1) -> float:
    # principal = начальный капитал (P)
    # rate = годовая ставка (r) в десятичной форме (5% = 0.05)
    # time = время в годах (t)
    # compounding = периоды начисления в год (n)
    """
    
    Formula: FV = P * (1 + r/n)^(n*t)
    
    
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


def present_value(future_value_amount: float, rate: float, time: float, #Расчет текущей стоимости ( сколько нужно вложить сегодня, чтобы получить нужную сумму в будущем)
                  compounding: int = 1) -> float:
    """
    
    Formula: PV = FV / (1 + r/n)^(n*t)
    
    
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


def compound_interest(principal: float, rate: float, time: float, #Расчет начисленных процентов(Рассчитывает только сумму заработанных процентов)
                      compounding: int = 1) -> float:
    """
    
    Formula: CI = P * [(1 + r/n)^(n*t) - 1]
    
    
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


def annual_rate(present_value: float, future_value: float, time: float, #Рассчитывает, какая ставка нужна для достижения цели
                compounding: int = 1) -> float:
    """    
    Formula: r = n * [(FV/PV)^(1/(n*t)) - 1]
    
    
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


def time_to_goal(principal: float, future_value: float, rate: float, #Рассчитывает, сколько времени потребуется для достижения финансовой цели
                 compounding: int = 1) -> float:
    """    
    Formula: t = log(FV/PV) / (n * log(1 + r/n)
    
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