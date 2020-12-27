# -*- coding: utf-8 -*-

import pandas as pd

from ._seasonal import *


def stl(inDF, ns, np):

    res = seasonal_decompose(inDF)

    # Each components can be accssed with:
    residual = res.resid
    seasonal = res.seasonal
    trend = res.trend

    # decomposed DF
    outDF = pd.concat([residual, seasonal, trend], axis=1, keys = ['residual','seasonal','trend'])
    return outDF

