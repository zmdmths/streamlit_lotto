import streamlit as st
import pandas as pd
from datetime import datetime as dt
import random

def getl():
    lotto = set()
    while(len(lotto)<6):
        n = random.randint(1, 46)
        lotto.add(n)
    return tuple(lotto)


st.title("로또 번호 ")

st.header("로또 번호를 생성")

button = st.button("생성하기")

if button:
    for i in range(1, 7):
        n = sorted(getl())
        st.subheader(f"번호{i}:{n}")
    st.write("시간:", dt.now().strftime('%Y-%m-%d %hh:%mm'))

