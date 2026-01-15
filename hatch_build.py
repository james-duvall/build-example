"""Hatchling custom build hook.""" # noqa: INP001

import lzma
import pickle
from pathlib import Path

from build_example import Example
from hatchling.builders.hooks.plugin.interface import BuildHookInterface

DATA_TXT = Path(__file__).parent / 'src/build_example/data.txt'
DATA_PKLZ = Path(__file__).parent / 'src/build_example/data.pklz'

def compile_data(data_text_file = DATA_TXT, data_pickle_file = DATA_PKLZ):
    """Compile source data from text format to Example class object.

    This is the key function that does all the building work.
    """
    with data_text_file.open('r') as file:
        example = Example()
        for word in file:
            example.insert_word(word)
    with lzma.open(data_pickle_file, 'wb') as file:
        pickle.dump(example, file)

class CustomBuildHook(BuildHookInterface):
    """To call this hook automatically during build, uncomment in pyproject.toml.

    [tool.hatch.build.targets.wheel.hooks.custom]
    """

    def initialize(self, _version, _build_data):
        """Call external build helper function.

        compile_data() is kept external so that it is easier to call it manually.
        """
        print(f"building for target: {self.target_name}") # noqa: T201
        compile_data()
