import streamlit as st
import time

# 页面配置
st.set_page_config(page_title="生日快乐", page_icon="🎂", layout="centered")

# 主标题
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🎉 张家和你在干啥？</h1>", unsafe_allow_html=True)

# 居中按钮
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("🎁 点我"):
        st.balloons()
        time.sleep(1.2)
        st.success("🎂 祝张家和10岁生日快乐！🎈")
