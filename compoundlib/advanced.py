

def future_value_with_contributions(initial: float, monthly_contrib: float,   #Будущая стоимость с регулярными взносами
                                    rate: float, years: float, 
                                    compounding: int = 12) -> float:
    """
   
    Examples:
        >>> future_value_with_contributions(1000, 100, 0.07, 10)
        17723.425044904487
    """
    from .basic import future_value
    
    fv_initial = future_value(initial, rate, years, compounding)
    
    # FV_annuity = PMT * [((1 + r/n)^(n*t) - 1) / (r/n)]
    monthly_rate = rate / compounding
    periods = compounding * years
    
    if monthly_rate == 0:
        fv_annuity = monthly_contrib * periods
    else:
        fv_annuity = monthly_contrib * (((1 + monthly_rate) ** periods - 1) / monthly_rate)
    
    return fv_initial + fv_annuity


def retirement_calculator(current_age: int, retirement_age: int,                       #Комплексный расчет пенсионных накоплений с учетом
                          current_savings: float, monthly_contribution: float,
                          annual_return: float, inflation_rate: float = 0.02) -> dict:
    """
    
  
    """
    years_to_retirement = retirement_age - current_age
    
    fv = future_value_with_contributions(
        current_savings, monthly_contribution, 
        annual_return, years_to_retirement
    )
    
    real_return = (1 + annual_return) / (1 + inflation_rate) - 1
    fv_in_todays_dollars = future_value_with_contributions(
        current_savings, monthly_contribution,
        real_return, years_to_retirement
    )
    
    safe_withdrawal = fv * 0.04
    safe_withdrawal_monthly = safe_withdrawal / 12
    
    return {
        'years_to_retirement': years_to_retirement,
        'future_value_nominal': round(fv, 2),
        'future_value_real': round(fv_in_todays_dollars, 2),
        'monthly_income_nominal': round(safe_withdrawal_monthly, 2),
        'monthly_income_real': round(safe_withdrawal_monthly / (1 + inflation_rate) ** years_to_retirement, 2),
        'total_contributions': round(monthly_contribution * 12 * years_to_retirement, 2),
        'total_interest': round(fv - current_savings - (monthly_contribution * 12 * years_to_retirement), 2)
    }


def loan_payment(principal: float, annual_rate: float, years: int, #Расчет платежей по кредиту
                 payments_per_year: int = 12) -> float:
    """
    
    Formula: PMT = P * [r(1+r)^n] / [(1+r)^n - 1]
    
   
    """
    periods = years * payments_per_year
    period_rate = annual_rate / payments_per_year
    
    if period_rate == 0:
        return principal / periods
    
    payment = (principal * period_rate * (1 + period_rate) ** periods) / \
              ((1 + period_rate) ** periods - 1)
    return payment


def investment_goal(target_amount: float, current_amount: float,                      #Расчет необходимых взносов
                    rate: float, years: float, compounding: int = 12) -> float:
    """
    
    
    
    Examples:
        >>> investment_goal(100000, 10000, 0.07, 10)
        503.7187305045641  # Monthly contribution needed
    """
    from .basic import future_value
    
    fv_current = future_value(current_amount, rate, years, compounding)
    
    if fv_current >= target_amount:
        return 0.0
    
    # formula: PMT = (FV * r/n) / [(1 + r/n)^(n*t) - 1]
    period_rate = rate / compounding
    periods = compounding * years
    
    if period_rate == 0:
        required = (target_amount - fv_current) / periods
    else:
        required = ((target_amount - fv_current) * period_rate) / \
                   ((1 + period_rate) ** periods - 1)
    
    return required
