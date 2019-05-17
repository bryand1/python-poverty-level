## U.S. Federal Poverty Guidelines

![license MIT](https://s3-us-west-1.amazonaws.com/bryand1/images/badges/license-MIT-blue.svg)
![python 3.6 | 3.7](https://s3-us-west-1.amazonaws.com/bryand1/images/badges/python-3.6-3.7.svg)


### Usage

```python
from poverty import PovertyLevel

pl = PovertyLevel()
pl.state = 'AK'
pl.get(household_size=3)  # 26660
pl.percent(income=26660, household_size=3) # 1.00
pl.below(income=26500, household_size=3)  # True

# You can also pass `state` as an argument
pl.get(household_size=3, state='New Jersey')  # 21330
pl.below(income=19000, household_size=3, state='New Jersey')  # True
```

### Resources

[Poverty Guidelines](https://aspe.hhs.gov/poverty-guidelines)  
