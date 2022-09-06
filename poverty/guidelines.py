"""
2019 U.S. Federal Poverty Limit Guidelines

https://aspe.hhs.gov/poverty-guidelines
"""

contiguous = {
    1: 13590,
    2: 18310,
    3: 23030,
    4: 27750,
    5: 32470,
    6: 37190,
    7: 41910,
    8: 46630,
}

hawaii = {
    1: 15630,
    2: 21060,
    3: 26490,
    4: 31920,
    5: 37350,
    6: 42780,
    7: 48210,
    8: 53640,
}

alaska = {
    1: 16990,
    2: 22890,
    3: 28790,
    4: 34690,
    5: 40590,
    6: 46490,
    7: 52390,
    8: 58290,
}

each_additional_member = {
    "contiguous": 4720,
    "hawaii": 5430,
    "alaska": 5900,
}
