"""
2019 U.S. Federal Poverty Limit Guidelines

https://aspe.hhs.gov/poverty-guidelines
"""

contiguous = {
    1: 12490,
    2: 16910,
    3: 21330,
    4: 25750,
    5: 30170,
    6: 34590,
    7: 39010,
    8: 43430,
}

hawaii = {
    1:	14380,
    2:	19460,
    3:	24540,
    4:	29620,
    5:	34700,
    6:	39780,
    7:	44860,
    8:	49940,
}

alaska = {
    1: 15600,
    2: 21130,
    3: 26660,
    4: 32190,
    5: 37720,
    6: 43250,
    7: 48780,
    8: 54310,
}

each_additional_member = {
    'contiguous': 4420,
    'hawaii': 5080,
    'alaska': 5530,
}
