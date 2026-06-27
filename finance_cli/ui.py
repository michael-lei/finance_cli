import streamlit as st


def render_sidebar(title):
    """渲染统一的侧边栏样式和内容"""
    st.markdown("""
<style>
    /* 隐藏自动生成的导航菜单 */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    [data-testid="stSidebar"] * {
        color: #e0e0e0 !important;
    }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {
        color: #ffffff !important;
    }
    section[data-testid="stSidebar"] > div:first-child > div:nth-child(2) {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

    st.sidebar.markdown("## 💰 记账工具")
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"### {title}")
    st.sidebar.markdown("")
    st.sidebar.page_link("app.py", label="🏠 首页", use_container_width=False)
    st.sidebar.page_link("pages/1_add.py", label="📝 添加账目", use_container_width=False)
    st.sidebar.page_link("pages/2_list.py", label="📋 查看列表", use_container_width=False)
    st.sidebar.page_link("pages/3_stats.py", label="📊 分类统计", use_container_width=False)
