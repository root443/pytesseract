import pandas as pd
from io import StringIO


class charframe:
    separator = " "

    def __init__(self, content):
        self._dataframe = pd.read_csv(StringIO(content), header=None, sep=self.separator)
        self._framestring = ""

    @property
    def dataframe(self):
         return self._dataframe

    @property
    def framestring(self):
        return self._dataframe.loc[:, 0].tolist()
