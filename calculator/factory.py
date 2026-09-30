"""Complete a Simple Factory. Creation must not execute the command."""
from calculator.commands import Command, ManualStdDevCommand, CsvStdDevCommand


class CommandFactory:
    @staticmethod
    def create(name: str, values=None) -> Command:
        # TODO: normalize the name, create a command, or raise ValueError.
        raise NotImplementedError("Implement factory selection")
