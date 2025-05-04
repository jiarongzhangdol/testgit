import streamlit as st
import pandas as pd
import requests

st.title("因子表现查询工具")

stock = st.text_input("输入股票代码", "600519")
factor = st.selectbox("选择因子", ["momentum", "volatility", "size", "value"])

if st.button("查询"):
    url = f"http://localhost:8000/api/getFactorStats?symbol={stock}&factor={factor}"
    res = requests.get(url)
    if res.status_code == 200:
        df = pd.DataFrame(res.json())
        st.dataframe(df)
        st.line_chart(df["IC"])  # 假设有个 IC 列
    else:
        st.error("查询失败")
