<<<<<<< HEAD
## Job Insights  

基于FastAPI + SQLModel的招聘信息平台后端原型,提供职位的查询、推荐、统计分析接口，并支持加载样例数据，快速展示完整的数据流

## 核心功能

### 职位管理

- `GET /jobs`：支持关键词搜索、城市过滤、分页

- `GET /jobs/recommend`：根据技能关键字推荐职位

### 统计分析

- `GET /stats/city`：统计各城市职位数量

- `GET /stats/salary`：按薪资区间（5k 档）统计职位分布

## 样例数据导入

- python -m app.utils.ingest --load-sample 自动从 CSV 加载测试数据

## 交互式文档

- 内置 Swagger UI → 访问 http://127.0.0.1:8000/docs

## 技术栈

- `后端框架`：FastAPI

- `ORM/建模`：SQLModel

- `数据库`：SQLite

- `数据处理`：Pandas（用于后续扩展统计分析）

- `测试`：Pytest + FastAPI TestClient

- `配置管理`：python-dotenv（支持多环境配置）

## 树结构
```
app/
 ├── main.py          # 应用入口，挂载路由
 ├── models.py        # SQLModel 数据模型 (Job)
 ├── database.py      # 数据库连接与会话管理
 ├── routers/         # jobs & stats API 路由
 └── utils/ingest.py  # 样例数据导入脚本
data/
 ├── jobs.db          # SQLite 数据库
 └── sample_jobs.csv  # 样例数据
tests/
 └── test_api.py      # 基础测试

## 演示

- 启动服务：uvicorn app.main:app --reload
- 访问文档：http://127.0.0.1:8000/docs
