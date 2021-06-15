'''An interface for a database containing divisor sums.'''

from abc import ABC
from abc import abstractmethod
from typing import List
from riemann.types import RiemannDivisorSum, SummaryStats


class DivisorDb(ABC):
    @abstractmethod
    def load() -> List[RiemannDivisorSum]:
        '''Load the entire database'''
        pass

    @abstractmethod
    def upsert(data: List[RiemannDivisorSum]) -> None:
        '''Insert or update the given list of data points.'''
        pass

    @abstractmethod
    def summarize() -> SummaryStats:
        '''Summarize the contents of the database.'''
        pass
