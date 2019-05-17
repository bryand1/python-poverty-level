from enum import Enum


class State(Enum):
    """There are three guidelines: contiguous 48 states, Hawaii, and Alaska"""
    HI = 'hawaii'
    AK = 'alaska'
    DC = 'contiguous'
    CONTIGUOUS = 'contiguous'
