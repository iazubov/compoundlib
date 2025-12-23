# test_manual.py
import sys
sys.path.insert(0, '.')

from compoundlib import *

# Тест базовых функций
print("=== Базовые функции ===")
print(f"Будущая стоимость: {future_value(1000, 0.05, 10):.2f}")
print(f"Сложный процент: {compound_interest(1000, 0.05, 10):.2f}")
print(f"Необходимое время для удвоения: {time_to_goal(1000, 2000, 0.07):.1f} лет")

# Тест расширенных функций
print("\n=== Расширенные функции ===")
print(f"С ежемесячными взносами: {future_value_with_contributions(1000, 100, 0.07, 10):.2f}")

retirement = retirement_calculator(30, 65, 50000, 500, 0.07)
print(f"\nПенсионные накопления: ${retirement['future_value_nominal']:,.2f}")
print(f"Ежемесячный доход на пенсии: ${retirement['monthly_income_nominal']:,.2f}")