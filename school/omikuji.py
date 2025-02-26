import streamlit as st
import random

st.title("おみくじアプリ")

if st.button("おみくじ"):
    num = random.randint(0, 4)
    st.write("乱数:", num)
    
    if num == 0:
        st.write("大当たり")
    elif num == 1:
        st.write("当たり")
    else:
        st.write("はずれ")
