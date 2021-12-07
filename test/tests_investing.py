from api_securities import get_df_by_stick
from api_securities import periods
import pandas

import pytest

def test_get_data():
    assert type(get_df_by_stick(8830, perion='15Min')) == pandas.DataFrame