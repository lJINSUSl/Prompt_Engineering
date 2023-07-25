import os
import json
import re
import streamlit as st
import pandas as pd
pd.options.mode.chained_assignment = None
import bardapi

st.title('Welcome to the Answer_Upgrader')

st.header('Input')
company = st.text_input("Please input your answering company")
input = st.text_input("Please input your given answer.")


def extract_urls(text):

  # url 패턴을 정의합니다.
  pattern = re.compile(r'(https?://[^\s]+)')

  # url을 추출합니다.
  urls = re.findall(pattern, text)

  if urls:
        return urls
  else:
        return None

urls = extract_urls(input)



txt = f"Here I give you 3 information. It contains 'name of the company', 'answer', 'hyperlink' if possible.\n{company}, {input}, {urls}\nAs you given 3 information file, you are now a counseler of the company. Improve 'answer' by using hyper link. If you can, search details in hyperlink. And show me previous answer and your answer so I can compare both."

os.environ['_BARD_API_KEY'] = 'YQh70kNxjPxZLaaftSj-8bAc4K3JTxG7SSAK3akGaCEi9oLGAfpXx8CGHxgEAJ9qXWUoOQ.'

if st.button('click to show improved answer'):
    con = st.container()
    con.caption("Result")
    con.write(bardapi.Bard().get_answer(f'{txt}')['content'])