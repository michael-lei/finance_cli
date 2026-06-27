# Python Web 记账工具 — 实现方案

## Context
用户需要一个个人记账 Web 工具，目标是简单易用、功能完整。用户是编程新手，需要结构清晰、代码不复杂。技术栈：Python + Streamlit + SQLite3。

## 项目结构

```
finance_cli/
├── app.py              # Streamlit 主入口，页面路由
├── database.py         # 数据库初始化 + CRUD 操作
├── pages/
│   ├── 1_add.py        # 添加账目页面
│   ├── 2_list.py       # 查看列表页面（筛选 + 表格 + 删除）
│   └── 3_stats.py      # 分类统计页面（柱状图 + 统计表）
└── requirements.txt    # streamlit
```

## 数据库设计

一个表 `records`，字段：

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER PRIMARY KEY AUTOINCREMENT | 自增 ID |
| amount | REAL NOT NULL | 金额（正数） |
| category | TEXT NOT NULL | 分类 |
| date | TEXT NOT NULL | 日期，格式 YYYY-MM-DD |
| note | TEXT | 备注，允许为空 |

预设 6 个分类：餐饮、交通、购物、娱乐、居住、其他。

## 各页面设计

### 1. 添加账目 (`pages/1_add.py`)
- 表单：金额（数字输入）、分类（下拉选择）、日期（日期选择器）、备注（文本输入）
- 提交按钮，成功后显示 `st.success`，清空表单
- 金额 > 0 前端校验

### 2. 查看列表 (`pages/2_list.py`)
- 顶部筛选栏：月份选择（年月）、分类多选
- 表格展示：ID、金额、分类、日期、备注，按日期降序
- 底部显示总金额
- 删除区：输入 ID + 删除按钮，二次确认弹窗，删除后刷新

### 3. 分类统计 (`pages/3_stats.py`)
- 月份筛选（同列表页）
- 柱状图：按分类汇总金额，用 `st.bar_chart`
- 统计表：分类、合计金额、占比、笔数
- 未筛选到数据时显示空状态提示

## database.py 函数清单

- `init_db()` — 建表（不存在则创建）
- `add_record(amount, category, date, note)` — 插入
- `get_records(month=None, categories=None)` — 按条件查询
- `delete_record(id)` — 按 ID 删除，返回是否成功
- `get_stats(month=None)` — 按分类汇总金额和笔数

月份筛选逻辑：若传 `month`（格式 `YYYY-MM`），则 `WHERE date LIKE 'YYYY-MM%'`。

## 关键细节

- `st.date_input` 返回 `date` 对象，入库时转字符串
- 分类用 `st.selectbox`（添加页）和 `st.multiselect`（筛选页）
- 柱状图数据直接用 `st.bar_chart(df.set_index("分类")["金额"])`
- 金额显示保留两位小数
- 收入/支出不区分——所有账目都是支出记录（后续可扩展）

## 依赖

```
streamlit
```

只需 streamlit，sqlite3 是 Python 内置库。

## 验证方式

1. `pip install streamlit` 安装依赖
2. `streamlit run app.py` 启动
3. 浏览器打开后测试完整流程：
   - 添加几条不同分类的账目
   - 在列表页按月份和分类筛选
   - 删除一条记录
   - 统计页查看柱状图和统计表
