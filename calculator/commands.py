"""Complete the Command pattern. Keep prompts out of these classes."""
from abc import ABC, abstractmethod
from calculator.statistics import standard_deviation


class Command(ABC):
    @abstractmethod
    def execute(self) -> float:
        """Return the result of the request."""


class ManualStdDevCommand(Command):
    def __init__(self, values):
        # TODO: store the request inputs.
        raise NotImplementedError("Implement manual construction")

    def execute(self) -> float:
        # TODO: delegate to standard_deviation.
        raise NotImplementedError("Implement manual execution")


class CsvStdDevCommand(Command):
    def __init__(self, path="values.csv"):
        # TODO: store the path; CLI users do not select a file.
        raise NotImplementedError("Implement CSV construction")

    def execute(self) -> float:
        # TODO: use pandas.read_csv, validate the value column, and delegate.
        raise NotImplementedError("Implement CSV execution")
