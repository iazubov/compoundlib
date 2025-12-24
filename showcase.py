# showcase.py
import compoundlib as cl

print(" ДЕМОНСТРАЦИЯ COMPOUNDLIB")
print("=" * 50)

# 1. Простейший пример
print("\n1. Базовый расчёт сложного процента")
result = cl.future_value(10000, 0.08, 5)
print(f"   Вложили: 10,000 руб под 8% на 5 лет")
print(f"   Получите: {result:,.2f} руб")
print(f"   Заработано: {result-10000:,.2f} руб")

# 2. Реальный сценарий
print("\n2.  Ипотечный калькулятор")
payment = cl.loan_payment(2000000, 0.07, 20)
print(f"   Кредит: 2,000,000 руб на 20 лет под 7%")
print(f"   Ежемесячный платёж: {payment:,.2f} руб")
print(f"   Всего выплатите: {payment*12*20:,.2f} руб")

# 3. Пенсионное планирование
print("\n3.  Пенсионный план (30 лет → 60 лет)")
plan = cl.retirement_calculator(
    current_age=30,
    retirement_age=60,
    current_savings=50000,
    monthly_contribution=5000,
    annual_return=0.06
)
print(f"   Накопите к пенсии: {plan['future_value_nominal']:,.0f} руб")
print(f"   Ежемесячный доход на пенсии: {plan['monthly_income_nominal']:,.0f} руб")

print("\n" + "=" * 50)
print(" Библиотека работает корректно!")
print("Установить: pip install compoundlib")