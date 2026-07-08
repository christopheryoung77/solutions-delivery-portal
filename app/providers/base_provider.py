"""
Atlas Base Provider

Abstract interface for all Atlas data providers.
"""

from abc import ABC, abstractmethod
from pandas import DataFrame


class BaseProvider(ABC):

    @abstractmethod
    def connect(self) -> None:
        """Connect to the data source."""
        ...

    @abstractmethod
    def disconnect(self) -> None:
        """Close the data source."""
        ...

    @abstractmethod
    def workbook_info(self) -> dict:
        """Return workbook metadata."""
        ...

    @abstractmethod
    def get_sheet(self, sheet_name: str) -> DataFrame:
        """Return a worksheet."""
        ...
