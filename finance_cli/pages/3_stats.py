import streamlit as st
import pandas as pd
from database import CATEGORIES, get_stats
from ui import render_sidebar

st.set_page_config(page_title="分类统计", page_icon="📊")
render_sidebar("📊 当前页面：分类统计")
st.title("📊 分类统计")

selected_month = st.text_input(
    "月份筛选（选填，格式 YYYY-MM）",
    placeholder="例如：2026-06",
)

rows = get_stats(month=selected_month if selected_month else None)

if not rows:
    st.info("暂无数据，先去添加几笔账目吧")
    st.stop()

df = pd.DataFrame(rows, columns=["分类", "金额", "笔数"])
total = df["金额"].sum()
df["占比"] = df["金额"].apply(lambda x: f"{x / total * 100:.1f}%")
df["金额"] = df["金额"].apply(lambda x: f"{x:.2f}")

# 柱状图
stat_data = pd.DataFrame(
    {r[0]: r[1] for r in rows}, index=["金额"]
).T.sort_values("金额", ascending=True)

st.subheader("柱状图")
st.bar_chart(stat_data, horizontal=True)

# 统计表
st.subheader("统计表")
total_display = f"{total:.2f}"
st.dataframe(df, hide_index=True, use_container_width=True)

st.markdown(f"**总支出：{total_display} 元**（共 {df['笔数'].sum():.0f} 笔）")
