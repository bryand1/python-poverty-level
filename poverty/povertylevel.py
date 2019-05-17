from . import guidelines
from .state import State


class PovertyLevel:

    def __init__(self):
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value: str):
        lower = value.lower()
        if lower in ('hi', 'hawaii'):
            self._state = State.HI
        elif lower in ('ak', 'alaska'):
            self._state = State.AK
        elif lower in ('dc', 'd.c.', 'washington dc', 'washington d.c.', 'district of columbia'):
            self._state = State.DC
        else:
            self._state = State.CONTIGUOUS

    def below(self, income: int, household_size: int, state: str = None) -> bool:
        """Is a person with this income and household size below the federal poverty limit?"""
        poverty_level = self.get(household_size, state)
        return income <= poverty_level

    def percent(self, income: int, household_size: int, state: str = None) -> float:
        """Income expressed as a percent of the federal poverty limit"""
        poverty_level = self.get(household_size, state)
        return round(income / poverty_level, 2)

    def get(self, household_size: int, state: str = None) -> int:
        """Get the U.S. federal poverty level based on household size and state"""
        if state is not None:
            self.state = state
        table = getattr(guidelines, self._state.value)
        additional_member_cost = guidelines.each_additional_member[self._state.value]
        additional_members = max(0, household_size - max(table.keys()))
        poverty_level = table[min(max(table.keys()), household_size)] + (additional_members * additional_member_cost)
        return poverty_level
