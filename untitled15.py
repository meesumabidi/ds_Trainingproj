# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 05:30:22 2020

@author: pc
"""

import Glassdoor_scrapper as gs 
import pandas as pd
path = "C:/Users/pc/Documents/ds_salary_proj/chromedriver"
df = gs.get_jobs('data scientist', 15, False, path, 15)
