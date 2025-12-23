# CompoundLib

[![Python Version](https://img.shields.io/pypi/pyversions/compoundlib)](https://pypi.org/project/compoundlib/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python library for compound interest calculations and financial planning.

## Features

- **Basic Calculations**: Future value, present value, compound interest
- **Advanced Functions**: Regular contributions, retirement planning, loan payments
- **Flexible Compounding**: Annual, quarterly, monthly, daily
- **Type Hints**: Full type annotations for better IDE support
- **Comprehensive Tests**: 100% test coverage for reliability

## Installation

```bash
pip install compoundlib

'## Quick Start'

'''from compoundlib import future_value, retirement_calculator

# Calculate future value
investment = future_value(principal=1000, rate=0.05, time=10)
print(f"Future value: ${investment:.2f}")

# Plan for retirement
plan = retirement_calculator(
    current_age=30,
    retirement_age=65,
    current_savings=50000,
    monthly_contribution=500,
    annual_return=0.07
)
print(f"Retirement savings: ${plan['future_value_nominal']:,.2f}")'''

'## Future Value Calculation'

'''from compoundlib import future_value, compound_interest

# Simple annual compounding
fv = future_value(1000, 0.05, 10)  # $1,628.89

# Monthly compounding
fv_monthly = future_value(1000, 0.05, 10, 12)  # $1,647.01

# Calculate interest earned
interest = compound_interest(1000, 0.05, 10)  # $628.89'''

'## Present Value'

from compoundlib import present_value

'''# How much to invest now to get $1000 in 5 years at 5%
pv = present_value(1000, 0.05, 5)  # $783.53'''

'## Time to Reach Goal'

'''from compoundlib import time_to_goal

# How long to double investment at 7%
years = time_to_goal(1000, 2000, 0.07)  # 10.24 years'''

'## Regular Contributions'

'''from compoundlib import future_value_with_contributions

# $1000 initial + $100 monthly for 10 years at 7%
total = future_value_with_contributions(
    initial=1000,
    monthly_contrib=100,
    rate=0.07,
    years=10
)  # $17,723.43'''

'## Retirement Planning'

'''from compoundlib import retirement_calculator

plan = retirement_calculator(
    current_age=35,
    retirement_age=65,
    current_savings=100000,
    monthly_contribution=1000,
    annual_return=0.06,
    inflation_rate=0.02
)

print(f"Years to retirement: {plan['years_to_retirement']}")
print(f"Future value: ${plan['future_value_nominal']:,.2f}")
print(f"Monthly retirement income: ${plan['monthly_income_nominal']:,.2f}")'''

'## Loan Calculations'

'''from compoundlib import loan_payment

# 30-year mortgage
payment = loan_payment(
    principal=200000,
    annual_rate=0.05,
    years=30
)  # $1,073.64 per month'''

'## Investment Goal Planning'

'Basic Module'

'''future_value(principal, rate, time, compounding=1)
Calculate future value with compound interest.

present_value(future_value, rate, time, compounding=1)
Calculate present value needed for future amount.

compound_interest(principal, rate, time, compounding=1)
Calculate interest earned through compounding.

annual_rate(present_value, future_value, time, compounding=1)
Calculate required annual rate to reach goal.

time_to_goal(principal, future_value, rate, compounding=1)
Calculate time needed to reach investment goal.'''

'## Advanced Module'

'''future_value_with_contributions(initial, monthly_contrib, rate, years, compounding=12)
Calculate future value with regular contributions.

retirement_calculator(current_age, retirement_age, current_savings, monthly_contribution, annual_return, inflation_rate=0.02)
Comprehensive retirement planning calculator.

loan_payment(principal, annual_rate, years, payments_per_year=12)
Calculate periodic loan payment amount.

investment_goal(target_amount, current_amount, rate, years, compounding=12)'''

' ## Setup Development Environment'

'''# Clone repository
git clone https://github.com/YOUR_USERNAME/compoundlib.git
cd compoundlib

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install development dependencies
pip install -e ".[dev]" '''

' ## Running Tests'

''' # Run all tests
pytest

# With coverage report
pytest --cov=compoundlib

# Specific test file
pytest tests/test_basic.py -v '''









