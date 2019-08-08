import pandas as pd
from io import StringIO


class charframe:
    separator = " "

    def __init__(self, content, header=False):
        if header:
            self._dataframe = pd.read_csv(StringIO(content), sep=self.separator)
        else:
            self._dataframe = pd.read_csv(StringIO(content), header=None, sep=self.separator)
        self._frame = self._dataframe.loc



    @property
    def dataframe(self):
        return self._dataframe

    def frame_from_col(self, column=0):
        return self._dataframe.loc[:, column].tolist()

    @property
    def frame(self):
        return self._frame[:]
