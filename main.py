from abc import ABC, abstractmethod
from enum import StrEnum


class InvalidUnit(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class UnitConverter(ABC):
    @abstractmethod
    def convert(self, from_unit: str, to_unit: str, value: float) -> float:
        print("successfull!!!...")

    @abstractmethod
    def unit_soported(self) -> list[str]:
        pass

    @abstractmethod
    def validate_unit(self) -> bool:
        pass


class MeterConverter(UnitConverter):
    def convert(self, from_unit: str, to_unit: str, value: float) -> float:
        print("successfull!!!")

    def unit_soported(self) -> list[str]:
        return ["kg", "cm", "m"]

    def validate_unit(self, unit: str) -> bool:
        return unit in self.unit_soported() or not isinstance(unit, str)


class App:
    def __init__(self, converter: UnitConverter):
        self.converter = converter

    def start(self, from_unit: str, to_unit: str, value: float):
        if not self.converter.validate_unit(
            from_unit
        ) or not self.converter.validate_unit(to_unit):
            raise InvalidUnit(
                message=f"Enter a valid unit, {self.converter.unit_soported()}"
            )
        self.converter.convert(from_unit, to_unit, value)


if __name__ == "__main__":
    m = MeterConverter()
    app1 = App(m)
    app1.start("m", "kg", 10)
