import glassdoor_scrapper as gs
import pandas as pd

path = "C:/Users/pc/OneDrive/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 15)

df
df.to_excel(r'C:/Users/pc/OneDrive/Documents/ds_salary_proj/project.xlsx', index = False)