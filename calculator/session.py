"""One deliberately defective method: repair execute-before-record ordering."""
from calculator.history import History


class CalculatorSession:
    def __init__(self):
        self._history = History()

    def calculate(self, calculation) -> float:
        # TODO BUG: recording a placeholder before execution pollutes history on
        # failure and saves the wrong result on success. Replace these two lines:
        # execute once, then record the actual successful result, then return it.
        self._history.add(calculation, 0.0)
        return calculation.get_result()

    def get_history(self):
        return self._history.get_history()

    def clear(self) -> None:
        self._history.clear()
