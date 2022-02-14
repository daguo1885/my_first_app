import streamlit as st
import time
import pandas as pd
import base64
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder

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
if sidebar == "项目管理":
    st.title("项目管理")
    # 项目选择框
    project_name = st.selectbox(
        "请选择项目",
        ["项目A", "项目B"]
    )
    if project_name:
        # 表单
        with st.form(project_name):
            project_info_1 = st.text_input("项目信息1", project_name)
            project_info_2 = st.text_input("项目信息2", project_name)
            project_info_3 = st.text_input("项目信息3", project_name)
            submitted = st.form_submit_button("提交")
            if submitted:
                # 在这里添加真实的业务逻辑
                # 这是一个进度条
                bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    bar.progress(i)
                st.write("项目信息1:%s, 项目信息2:%s, 项目信息3:%s" % (project_info_1, project_info_2, project_info_3))
                st.success("提交成功")
elif sidebar == "用户管理":
    st.title("用户管理")
    # 将页面分为左半边和右半边
    left, right = st.beta_columns(2)
    # 左半边页面展示部分
    with left:
        st.header("查看、更新用户信息")
        user_name = st.selectbox(
            "请选择用户",
            ["郑立赛", "乔布斯", "王大拿"]
        )
        if user_name:
            with st.form(user_name):
                phone_num = st.text_input("手机号", user_name)
                role = st.multiselect(
                    "用户角色",
                    ["大神", "大拿"],
                    ["大神"]
                )
                user_group = st.multiselect(
                    "请选择用户组",
                    ["大神组", "大拿组"],
                    ["大神组"]
                )
                submitted = st.form_submit_button("提交")
                if submitted:
                    # 这里添加真实的业务逻辑
                    st.write("用户名:%s, 手机号:%s, 用户角色:%s, 用户组:%s" % (user_name, phone_num, role, user_group))
                    st.success("提交成功")
    # 右半边页面展示部分
    with right:
        st.header("添加、删除用户")
        user_action = st.selectbox(
            "请选择操作",
            ["添加用户", "删除用户"]
        )
        if user_action:
            with st.form(user_action):
                if user_action == "添加用户":
                    phone_num = st.text_input("手机号", user_name)
                    role = st.multiselect(
                        "用户角色",
                        ["大神", "大拿"]
                    )
                    user_group = st.multiselect(
                        "请选择用户组",
                        ["大神组", "大拿组"]
                    )
                    submitted = st.form_submit_button("提交")
                    if submitted:
                        # 请在这里添加真实业务逻辑，或者单独写一个业务逻辑函数
                        st.write("user_name:%s, phone_num:%s, role:%s, user_group:%s" % (user_name, phone_num, role, user_group))
                        st.success("提交成功")
                else:
                    user_group = st.multiselect(
                        "请选择要删除的用户",
                        ["郑立赛", "乔布斯", "王大拿"]
                    )
                    submitted = st.form_submit_button("提交")
                    if submitted:
                        # 请在这里添加真实业务逻辑，或者单独写一个业务逻辑函数
                        st.write("user_name:%s, phone_num:%s, role:%s, user_group:%s" % (user_name, phone_num, role, user_group))
                        st.success("提交成功")
elif sidebar == "权限管理":
    st.title("权限管理")
    with st.form("auth"):
        user = st.multiselect(
            "选择用户",
            ["郑立赛", "乔布斯", "王大拿"]
        )
        role = st.multiselect(
            "选择用户角色",
            ["大神", "大拿"]
        )
        user_group = st.multiselect(
            "请选择用户组",
            ["大神组", "大拿组"]
        )
        submitted = st.form_submit_button("提交")
        if submitted:
            # 请在这里添加真实业务逻辑，或者单独写一个业务逻辑函数
            st.write(
                "用户:%s, 角色:%s, 用户组:%s" % (user, role, user_group))
            st.success("提交成功")
else:
    st.title("运维管理后台")
    st.write("欢迎使用运维管理后台")

# st.sidebar.title("核酸检查")
sidebar2 = st.sidebar.selectbox(
    "核酸检查",
    ("功能选择", "数据下载", "当日统计", "次日检查", "生成报表")
)
if sidebar2 == "数据下载":
    file = st.file_uploader("选择上传表格", type=['.xlsx', '.xls'])
    if (file is not None) and file.name.endswith('.xlsx'):
        try:
            df = pd.read_excel(file, converters={'员工号': str}).fillna('')
        except:
            st.write("文件读取错误！")
        # file.close()
        st.dataframe(df)
        # (df.iloc[:, 0:9], fit_columns_on_grid_load=True)
        # b64 = df.to_csv()
        # st.markdown(f"<a href='localhost:8501\\test.py'>Download File</a>", unsafe_allow_html=True)
        fil = df.to_excel('xx.xlsx', index=False)
        st.download_button(
            label="Save as excel",
            data=fil,
            file_name='df_file.xlsx',
            mime='txt/csv'
        )
elif sidebar2 == '当日统计':
    tx = st.text_area("请输入AC检查结果文本", height=400)
    def s(tx):
        st.write(tx)
    st.button('运算', on_click=s(tx))
    xa = st.expander
    st.expander.write('sgksljklsfjkakjf;skdfj;a')
    st.expander.text_input('测试数撒')
    # st.write(xa)
    # st.text('测试文本')
elif sidebar2 == '次日检查':
    st.sidebar.text("只是一个测试")
    st.markdown("## Markdown 功能测试")
    st.info('teswt')
    a, b = st.columns([3, 1])
    with a:
        st.markdown("## Markdown 功能测试")
    with b:
        st.write("右侧区域")
    st.write("又开始新的一行")

    # file.close()
    # st.dataframe(df)
# st.sidebar.title("派遣检查")
sidebar3 = st.sidebar.selectbox(
    "派遣检查",
    ["功能选择", "连飞四天风险", "新乘带飞检查", "飞行小时监控", "SOC法规"]
)
st.sidebar.title("排班公平")
sidebar4 = st.sidebar.date_input(
    "排班公平"
)