

__version__ = "0.1.0"
__author__ = "Ваше Имя"
__email__ = "ваш.email@example.com"

# Импортируем основные функции для удобного доступа
from .basic import (
    future_value,
    present_value,
    compound_interest,
    annual_rate,
    time_to_goal
)

from .advanced import (
    future_value_with_contributions,
    retirement_calculator,
    loan_payment,
    investment_goal
)

# Что будет доступно при импорте через from compoundlib import *
__all__ = [
    'future_value',
    'present_value',
    'compound_interest',
    'annual_rate',
    'time_to_goal',
    'future_value_with_contributions',
    'retirement_calculator',
    'loan_payment',
    'investment_goal'
]
