from poverty import PovertyLevel
from poverty.guidelines import hawaii, alaska, contiguous, each_additional_member


def test_povertylevel_guidelines():
    pl = PovertyLevel()
    pl.state = 'HI'
    assert pl.get(1) == hawaii[1]

    pl.state = 'alaska'
    assert pl.get(2) == alaska[2]

    pl.state = 'ak'
    assert pl.get(3) == alaska[3]

    pl.state = 'district of columbia'
    assert pl.get(4) == contiguous[4]

    pl.state = 'arkansas'
    assert pl.get(5) == contiguous[5]

    pl.state = 'CA'
    assert pl.get(9) == contiguous[8] + each_additional_member['contiguous']

    assert pl.get(3, 'NJ') == contiguous[3]


def test_povertylevel_percent():
    pl = PovertyLevel()
    assert pl.percent(12490, 1, state='New Jersey') == 1.00
    assert pl.percent(14380, 1, state='Hawaii') == 1.00
