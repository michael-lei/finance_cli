import streamlit as st
from database import init_db
from ui import render_sidebar

st.set_page_config(page_title="记账工具", page_icon="💰")
init_db()

render_sidebar("🏠 首页")

st.title("💰 记账工具")

st.markdown("欢迎使用个人记账工具！")

col1, col2, col3 = st.columns(3)
with col1:
    st.page_link("pages/1_add.py", label="📝 添加账目", use_container_width=True)
with col2:
    st.page_link("pages/2_list.py", label="📋 查看列表", use_container_width=True)
with col3:
    st.page_link("pages/3_stats.py", label="📊 分类统计", use_container_width=True)
