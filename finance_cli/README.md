# 💰 记账工具

一个简单易用的个人记账 Web 工具，基于 Python + Streamlit + SQLite3。

## 功能

- **📝 添加账目** — 金额、分类、日期、备注，表单填写
- **📋 查看列表** — 按月份和分类筛选，每行支持修改和删除
- **📊 分类统计** — 柱状图 + 统计表，直观查看支出分布

预设 6 个分类：餐饮、交通、购物、娱乐、居住、其他。

## 快速开始

```bash
pip install streamlit
streamlit run app.py
```

浏览器访问 http://localhost:8501

## 项目结构

```
├── app.py           # 主页入口
├── database.py      # 数据库操作
├── ui.py            # 侧边栏样式
├── pages/
│   ├── 1_add.py     # 添加账目
│   ├── 2_list.py    # 查看列表
│   └── 3_stats.py   # 分类统计
└── requirements.txt
```

## 技术栈

- Python 3
- Streamlit
- SQLite3
