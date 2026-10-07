import pytest

from calculator.operations import Operations
from calculator.factory import CalculationFactory
from calculator.session import CalculatorSession
from calculator.commands import LastCommand


def test_adjust_with_offset_and_scale():
    assert Operations.adjust(3, offset=2, scale=4) == 20


def test_adjust_uses_default_values():
    assert Operations.adjust(5) == 5


def test_span_returns_difference_between_max_and_min():
    assert Operations.span(-4, 3, 8) == 12


def test_span_rejects_single_value():
    with pytest.raises(ValueError):
        Operations.span(5)


def test_factory_creates_adjust_calculation():
    calculation = CalculationFactory.create(
        "adjust",
        3,
        offset=2,
        scale=4
    )
    assert calculation.get_result() == 20


def test_last_returns_latest_successful_result():
    session = CalculatorSession()

    calculation = CalculationFactory.create(
        "adjust",
        3,
        offset=2,
        scale=4
    )

    session.calculate(calculation)

    assert LastCommand(session).execute() == (
        "adjust 3.0 offset=2.0 scale=4.0 = 20.0000"
    )


def test_failed_calculation_is_not_saved_to_history():
    session = CalculatorSession()

    calculation = CalculationFactory.create("divide", 5, 0)

    with pytest.raises(ZeroDivisionError):
        session.calculate(calculation)

    assert session.get_history() == []