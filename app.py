
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="记账本", page_icon="💰")

st.title("📒 手机记账本")

# 初始化记录存储
if "records" not in st.session_state:
    st.session_state["records"] = []

# 输入区域
amount = st.number_input("💰 花了多少钱", min_value=0.0, step=0.01)
category = st.text_input("📂 用途分类")
if st.button("记录一下"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state["records"].append(f"{now} | {category} | {amount:.2f} 元")
    st.success("✅ 已记录！")

# 展示记录
st.markdown("### 📑 所有记录：")
if st.session_state["records"]:
    for line in st.session_state["records"]:
        st.write(line)
else:
    st.write("暂无记录")
