

import pytest
from compoundlib.basic import (
    future_value,
    present_value,
    compound_interest,
    annual_rate,
    time_to_goal
)

class TestFutureValue:
    """Tests for future_value function."""
    
    def test_future_value_simple(self):
        """Test simple annual compounding."""
        # 1000 руб под 5% годовых на 10 лет
        result = future_value(1000, 0.05, 10)
        expected = 1000 * (1 + 0.05) ** 10
        assert result == pytest.approx(expected)
    
    def test_future_value_monthly(self):
        """Test monthly compounding."""
        result = future_value(1000, 0.05, 10, 12)
        expected = 1000 * (1 + 0.05/12) ** (12*10)
        assert result == pytest.approx(expected)
    
    def test_future_value_zero_rate(self):
        """Test with zero interest rate."""
        result = future_value(1000, 0, 10)
        assert result == 1000
    
    def test_future_value_zero_time(self):
        """Test with zero time."""
        result = future_value(1000, 0.05, 0)
        assert result == 1000
    
    def test_future_value_negative_inputs(self):
        """Test with negative values."""
        with pytest.raises(ValueError):
            future_value(-1000, 0.05, 10)
        
        with pytest.raises(ValueError):
            future_value(1000, -0.05, 10)
        
        with pytest.raises(ValueError):
            future_value(1000, 0.05, -10)


class TestPresentValue:
    """Tests for present_value function."""
    
    def test_present_value_simple(self):
        """Test present value calculation."""
        # Какая сумма сейчас нужна, чтобы получить 1000 через 5 лет под 5%
        result = present_value(1000, 0.05, 5)
        expected = 1000 / (1 + 0.05) ** 5
        assert result == pytest.approx(expected)
    
    def test_present_value_inverse(self):
        """Test that PV and FV are inverse operations."""
        pv = 1000
        rate = 0.05
        time = 10
        
        fv = future_value(pv, rate, time)
        pv_calculated = present_value(fv, rate, time)
        
        assert pv_calculated == pytest.approx(pv)


class TestCompoundInterest:
    """Tests for compound_interest function."""
    
    def test_compound_interest_simple(self):
        """Test compound interest calculation."""
        result = compound_interest(1000, 0.05, 10)
        fv = future_value(1000, 0.05, 10)
        expected = fv - 1000
        assert result == pytest.approx(expected)
    
    def test_compound_interest_zero(self):
        """Test with zero interest."""
        result = compound_interest(1000, 0, 10)
        assert result == 0


class TestAnnualRate:
    """Tests for annual_rate function."""
    
    def test_annual_rate_simple(self):
        """Test annual rate calculation."""
        # Какая ставка нужна, чтобы 1000 превратилось в 2000 за 10 лет
        result = annual_rate(1000, 2000, 10)
        
        # Проверяем, что рассчитанная ставка даёт нужный результат
        fv = future_value(1000, result, 10)
        assert fv == pytest.approx(2000)
    
    def test_annual_rate_rule_of_72(self):
        """Test against Rule of 72 approximation."""
        # По правилу 72: время удвоения ≈ 72 / процентная ставка
        rate = 0.07  # 7%
        time_to_double = 72 / 7  # ≈10.29 лет
        
        calculated_rate = annual_rate(1000, 2000, time_to_double)
        assert calculated_rate == pytest.approx(rate, rel=0.01)  # 1% погрешность


class TestTimeToGoal:
    """Tests for time_to_goal function."""
    
    def test_time_to_goal_doubling(self):
        """Test time to double investment."""
        result = time_to_goal(1000, 2000, 0.07)
        
        # Проверяем, что за это время действительно достигается цель
        fv = future_value(1000, 0.07, result)
        assert fv == pytest.approx(2000)
    
    def test_time_to_goal_rule_of_72(self):
        """Compare with Rule of 72."""
        rate = 0.09  # 9%
        rule_of_72 = 72 / 9  # 8 лет
        
        exact = time_to_goal(1000, 2000, rate)
        # Правило 72 даёт приближение в пределах 10%
        assert abs(exact - rule_of_72) / exact < 0.1


def test_error_handling():
    """Test error handling for invalid inputs."""
    # Тестируем добавление проверок (позже добавим в код)
    pass
