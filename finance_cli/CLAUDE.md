# 记账工具 — CLAUDE.md

## 启动

```bash
streamlit run app.py
```

浏览器访问 http://localhost:8501

## 项目结构

```
├── app.py               # 主页入口，初始化数据库
├── database.py          # SQLite3 操作（CRUD + 统计）
├── pages/
│   ├── 1_add.py         # 添加账目表单
│   ├── 2_list.py        # 查看/筛选/删除账目
│   └── 3_stats.py       # 分类统计（柱状图 + 统计表）
├── requirements.txt     # 依赖（仅 streamlit）
└── PLAN.md              # 实现方案
```

## 数据库

- SQLite3，文件 `finance.db` 自动生成
- 表 `records`：id, amount, category, date, note
- 预设 6 个分类：餐饮、交通、购物、娱乐、居住、其他

## 添加新功能

所有数据库操作写在 `database.py`，页面逻辑写在 `pages/` 下。
