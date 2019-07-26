import collections
from pprint import pprint

Scientists = collections.namedtuple('Scientists', [
    'name',
    'field',
    'born',
    'nobel'
])

scientists = (
    Scientists(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientists(name='Emmy Noether', field='math', born=1882, nobel=False),
)

fs = tuple(filter(lambda x: x.nobel is True, scientists))

next(fs)

pprint(scientists)