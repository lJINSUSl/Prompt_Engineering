import os
import json
import pandas as pd
import re

import string
pd.options.mode.chained_assignment = None
import bardapi

with open('twitter_data/twcs_small.json') as f:
    data = json.load(f)

record = data[0]

txt = f"Here I give you json file. It contains 'name of the company', 'answer', 'hyperlink' if possible.\n{record}\nAs you given json file, you are now a counseler of the company. Improve 'answer' by using hyper link. If you can, search details in hyperlink. And show me previous answer and your answer so I can compare both."

os.environ['_BARD_API_KEY'] = 'YQh70kNxjPxZLaaftSj-8bAc4K3JTxG7SSAK3akGaCEi9oLGAfpXx8CGHxgEAJ9qXWUoOQ.'

print(bardapi.Bard().get_answer(f'{txt}')['content'])
