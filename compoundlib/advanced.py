

def future_value_with_contributions(initial: float, monthly_contrib: float, 
                                    rate: float, years: float, 
                                    compounding: int = 12) -> float:
    """
    Calculate future value with regular monthly contributions.
    
    Formula combines future value of initial investment 
    and future value of annuity (regular contributions).
    
    Args:
        initial: Initial investment
        monthly_contrib: Monthly contribution amount
        rate: Annual interest rate (decimal)
        years: Investment period in years
        compounding: Compounding periods per year (default 12 for monthly)
    
    Returns:
        Total future value
    
    Examples:
        >>> future_value_with_contributions(1000, 100, 0.07, 10)
        17723.425044904487
    """
    from .basic import future_value
    
    # Future value of initial investment
    fv_initial = future_value(initial, rate, years, compounding)
    
    # Future value of annuity (regular contributions)
    # FV_annuity = PMT * [((1 + r/n)^(n*t) - 1) / (r/n)]
    monthly_rate = rate / compounding
    periods = compounding * years
    
    if monthly_rate == 0:
        fv_annuity = monthly_contrib * periods
    else:
        fv_annuity = monthly_contrib * (((1 + monthly_rate) ** periods - 1) / monthly_rate)
    
    return fv_initial + fv_annuity


def retirement_calculator(current_age: int, retirement_age: int, 
                          current_savings: float, monthly_contribution: float,
                          annual_return: float, inflation_rate: float = 0.02) -> dict:
    """
    Calculate retirement savings projections.
    
    Args:
        current_age: Current age
        retirement_age: Planned retirement age
        current_savings: Current retirement savings
        monthly_contribution: Monthly contribution to retirement
        annual_return: Expected annual return (decimal)
        inflation_rate: Expected inflation rate (decimal, default 2%)
    
    Returns:
        Dictionary with retirement projections
    """
    years_to_retirement = retirement_age - current_age
    
    # Calculate future value at retirement
    fv = future_value_with_contributions(
        current_savings, monthly_contribution, 
        annual_return, years_to_retirement
    )
    
    # Adjust for inflation (in today's dollars)
    real_return = (1 + annual_return) / (1 + inflation_rate) - 1
    fv_in_todays_dollars = future_value_with_contributions(
        current_savings, monthly_contribution,
        real_return, years_to_retirement
    )
    
    # Safe withdrawal amount (4% rule)
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


def loan_payment(principal: float, annual_rate: float, years: int, 
                 payments_per_year: int = 12) -> float:
    """
    Calculate loan payment (mortgage, car loan, etc.).
    
    Formula: PMT = P * [r(1+r)^n] / [(1+r)^n - 1]
    
    Args:
        principal: Loan amount
        annual_rate: Annual interest rate (decimal)
        years: Loan term in years
        payments_per_year: Payments per year (default 12 for monthly)
    
    Returns:
        Payment amount per period
    
    Examples:
        >>> loan_payment(200000, 0.05, 30)
        1073.6432467624878  # Monthly payment
    """
    periods = years * payments_per_year
    period_rate = annual_rate / payments_per_year
    
    if period_rate == 0:
        return principal / periods
    
    payment = (principal * period_rate * (1 + period_rate) ** periods) / \
              ((1 + period_rate) ** periods - 1)
    return payment


def investment_goal(target_amount: float, current_amount: float, 
                    rate: float, years: float, compounding: int = 12) -> float:
    """
    Calculate required monthly contribution to reach investment goal.
    
    Args:
        target_amount: Desired future amount
        current_amount: Current investment amount
        rate: Expected annual return (decimal)
        years: Time until goal (years)
        compounding: Compounding periods per year
    
    Returns:
        Required monthly contribution
    
    Examples:
        >>> investment_goal(100000, 10000, 0.07, 10)
        503.7187305045641  # Monthly contribution needed
    """
    from .basic import future_value
    
    # Future value of current amount
    fv_current = future_value(current_amount, rate, years, compounding)
    
    # If already reached goal
    if fv_current >= target_amount:
        return 0.0
    
    # Calculate required contribution
    # Using formula for annuity: PMT = (FV * r/n) / [(1 + r/n)^(n*t) - 1]
    period_rate = rate / compounding
    periods = compounding * years
    
    if period_rate == 0:
        required = (target_amount - fv_current) / periods
    else:
        required = ((target_amount - fv_current) * period_rate) / \
                   ((1 + period_rate) ** periods - 1)
    
    return required
