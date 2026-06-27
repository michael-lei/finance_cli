import streamlit as st
from datetime import date
from database import CATEGORIES, add_record
from ui import render_sidebar

st.set_page_config(page_title="添加账目", page_icon="📝")
render_sidebar("📝 当前页面：添加账目")
st.title("📝 添加账目")

with st.form("add_form", clear_on_submit=True):
    amount = st.number_input(
        "金额（元）",
        min_value=0.01,
        step=0.01,
        format="%.2f",
        placeholder="请输入金额",
    )
    category = st.selectbox("分类", CATEGORIES)
    date_val = st.date_input("日期", value=date.today())
    note = st.text_input("备注（可选）", placeholder="例如：午餐、地铁卡充值")
    submitted = st.form_submit_button("添加", type="primary", use_container_width=True)

    if submitted:
        if amount <= 0:
            st.error("金额必须大于 0")
        else:
            add_record(amount, category, date_val.isoformat(), note)
            st.success(f"已添加：{category} {amount:.2f} 元")
