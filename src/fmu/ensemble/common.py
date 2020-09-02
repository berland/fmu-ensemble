"""Mapping from fmu-ensemble custom offset strings to Pandas DateOffset strings.

See
https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects
"""
PD_FREQ_MNEMONICS = {
    "monthly": "MS",
    "yearly": "YS",
    "daily": "D",
    "weekly": "W-MON",
}

