import streamlit as st
import time
import pandas as pd


# 设置网页标题，以及使用宽屏模式
st.set_page_config(
    page_title="运维管理后台",
    layout="wide"
)

def download_excel(name, df):
    excel = df.to_excel(index=False)
    base = base64.b64encode(excel.encode()).decode()
    # file = (f'Download file'%(name))
    return base


# 隐藏右边的菜单以及页脚
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def index_page():
    st.empty()
    return True

# 左边导航栏
st.sidebar.title("数据维护")
st.sidebar.button("首页", on_click=index_page())
sidebar = st.sidebar.selectbox(
    "数据维护",
    ("功能选择", "项目管理", "用户管理", "权限管理")
)
