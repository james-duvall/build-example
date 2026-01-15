"""Minimal working example of 'recursive' build requirement.

The 'Example' class includes and internal data structure with a method to read source
text data into the internal structure.

At build time, an external source data file is read by the class and pickled for loading
at import time.
"""

import lzma
import pickle
import warnings
from pathlib import Path

from .example import Example

DATA_FILE = Path(__file__).parent / 'data.pklz'

try:
    with lzma.open(DATA_FILE, 'rb') as data:
        # let's assume we have properly validated that the data is safe to load.
        example = pickle.load(data) # noqa: S301
except (FileNotFoundError, pickle.PickleError) as e:
    msg = f"Pickled data is not present (this is OK during manual build).\n    {e}"
    warnings.warn(msg, stacklevel = 2)
    # the purpose of catching this error and converting to a warning is to allow the
    # package to successfully import the Example class during build time. During import
    # time, the pickled data should always be present and valid.
