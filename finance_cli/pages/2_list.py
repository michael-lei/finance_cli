import streamlit as st
from datetime import date
from database import CATEGORIES, get_records, get_record, update_record, delete_record
from ui import render_sidebar

st.set_page_config(page_title="查看列表", page_icon="📋")
render_sidebar("📋 当前页面：查看列表")
st.title("📋 查看列表")

# 筛选区
col1, col2 = st.columns(2)
with col1:
    selected_month = st.text_input(
        "月份筛选（选填，格式 YYYY-MM）",
        placeholder="例如：2026-06",
    )
with col2:
    selected_categories = st.multiselect(
        "分类筛选（不选则显示全部）",
        CATEGORIES,
    )

# 查数据
rows = get_records(
    month=selected_month if selected_month else None,
    categories=selected_categories if selected_categories else None,
)

if not rows:
    st.info("暂无数据，先去添加几笔账目吧")
    st.stop()

# 表头
hdr = st.columns([2, 1.5, 1.5, 2.5, 1.2, 1.2])
for col, text in zip(hdr, ["金额", "分类", "日期", "备注", "", ""]):
    col.markdown(f"**{text}**")

total = 0
for r in rows:
    record_id, amount, category, rec_date, note = r
    total += amount

    col1, col2, col3, col4, col5, col6 = st.columns([2, 1.5, 1.5, 2.5, 1.2, 1.2])
    col1.write(f"{amount:.2f}")
    col2.write(category)
    col3.write(rec_date)
    col4.write(note or "-")
    if col5.button("✏️ 修改", key=f"edit_{record_id}", use_container_width=True):
        st.session_state[f"edit_open_{record_id}"] = True
        st.session_state[f"del_confirm_{record_id}"] = False
        st.rerun()
    if col6.button("🗑️ 删除", key=f"del_{record_id}", use_container_width=True):
        st.session_state[f"del_confirm_{record_id}"] = True
        st.session_state[f"edit_open_{record_id}"] = False
        st.rerun()

    # 修改展开
    if st.session_state.get(f"edit_open_{record_id}"):
        with st.container():
            st.markdown("---")
            cols = st.columns([1, 1])
            with cols[0]:
                edit_amount = st.number_input("金额", value=amount, min_value=0.01, step=0.01, format="%.2f", key=f"ea_{record_id}")
                edit_category = st.selectbox("分类", CATEGORIES, index=CATEGORIES.index(category) if category in CATEGORIES else 0, key=f"ec_{record_id}")
            with cols[1]:
                try:
                    default_d = date.fromisoformat(rec_date)
                except ValueError:
                    default_d = date.today()
                edit_date = st.date_input("日期", value=default_d, key=f"ed_{record_id}")
                edit_note = st.text_input("备注", value=note or "", key=f"en_{record_id}")

            btn_row = st.columns([1, 1, 6])
            if btn_row[0].button("保存", type="primary", key=f"save_{record_id}"):
                update_record(record_id, edit_amount, edit_category, edit_date.isoformat(), edit_note)
                st.success(f"已修改 ID {record_id}")
                st.session_state[f"edit_open_{record_id}"] = False
                st.rerun()
            if btn_row[1].button("取消", key=f"cancel_{record_id}"):
                st.session_state[f"edit_open_{record_id}"] = False
                st.rerun()
            st.markdown("---")

    # 删除确认
    if st.session_state.get(f"del_confirm_{record_id}"):
        st.warning(f"确定删除 ID {record_id}（{category} {amount:.2f} 元）？")
        btn_row = st.columns([1, 1, 6])
        if btn_row[0].button("确认删除", type="primary", key=f"confirm_del_{record_id}"):
            delete_record(record_id)
            st.success(f"已删除 ID {record_id}")
            st.session_state[f"del_confirm_{record_id}"] = False
            st.rerun()
        if btn_row[1].button("取消", key=f"cancel_del_{record_id}"):
            st.session_state[f"del_confirm_{record_id}"] = False
            st.rerun()

st.markdown(f"**合计：{total:.2f} 元**（共 {len(rows)} 笔）")
