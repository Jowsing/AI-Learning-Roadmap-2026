# 🚀 AI Engineer Roadmap 2026

> 从零开始，系统成长为能够独立设计、开发、部署 AI 应用的工程师。

本仓库用于记录我的 AI 工程师学习路线、技术笔记、代码示例与项目实践。学习过程坚持 **30% 理论 + 70% 实践**，以可运行、可测试、可部署、可展示的项目作为阶段成果。

## 📌 目录

- [项目目标](#-项目目标)
- [学习路线](#️-学习路线)
- [9 个月学习计划](#️-9-个月学习计划)
- [专项学习计划](#-专项学习计划)
- [学习清单](#-学习清单)
- [项目规划](#-项目规划)
- [仓库结构](#️-仓库结构)
- [学习节奏](#-学习节奏)
- [项目交付标准](#-项目交付标准)
- [推荐资源](#-推荐资源)
- [最终目标](#-最终目标)

## 🎯 项目目标

- [ ] 熟练使用 Python 开发工程化应用
- [ ] 掌握 Git、Linux、Docker 与常见开发工作流
- [ ] 使用 FastAPI、PostgreSQL、Redis 构建 Web 服务
- [ ] 熟悉主流大模型 API、流式响应、结构化输出与工具调用
- [ ] 独立开发 RAG、Agent、MCP 等 AI 应用
- [ ] 完成开源模型的本地部署与 API 封装
- [ ] 掌握基础前端能力，能够交付完整 AI 产品
- [ ] 建立包含文档、测试、部署说明和演示的作品集
- [ ] 阅读优秀开源项目并尝试贡献代码

## 🗺️ 学习路线

```text
Python
  ↓
Git + Linux + Docker
  ↓
FastAPI + PostgreSQL + Redis
  ↓
LLM API + Prompt Engineering
  ↓
Streaming + Structured Output + Tool Calling
  ↓
RAG + Vector Database + Re-ranking
  ↓
Agent + LangGraph
  ↓
MCP
  ↓
React + TypeScript + Next.js
  ↓
Ollama + vLLM + SGLang
  ↓
测试 + 可观测性 + CI/CD
  ↓
企业级 AI 综合项目
```

## 🗓️ 9 个月学习计划

状态说明：`⬜ 未开始` · `🟨 进行中` · `✅ 已完成`

| 月份    | 阶段                | 核心内容                                         | 阶段成果                | 状态 |
| ------- | ------------------- | ------------------------------------------------ | ----------------------- | ---- |
| 第 1 月 | Python 与计算机基础 | 语法、OOP、typing、asyncio、文件处理、pandas     | 文件与 Excel 自动化工具 | ⬜   |
| 第 2 月 | 工程基础            | Git、Linux、Shell、Docker、Compose               | 容器化 Python 服务      | ⬜   |
| 第 3 月 | Web 后端            | FastAPI、SQLAlchemy、PostgreSQL、Redis、JWT      | 带认证的博客 API        | ⬜   |
| 第 4 月 | LLM 应用开发        | 模型基础、Prompt、流式响应、结构化输出、工具调用 | 多轮聊天机器人          | ⬜   |
| 第 5 月 | RAG                 | 文档解析、Embedding、向量检索、混合检索、重排    | 企业知识库              | ⬜   |
| 第 6 月 | Agent 与 MCP        | LangGraph、状态、记忆、工作流、MCP Client/Server | AI 办公助手             | ⬜   |
| 第 7 月 | 模型部署            | Ollama、vLLM、SGLang、GPU、量化、LoRA            | 本地模型 API 服务       | ⬜   |
| 第 8 月 | 前端与全栈          | React、TypeScript、Next.js、流式 UI、文件上传    | ChatGPT Clone           | ⬜   |
| 第 9 月 | 综合实战            | 测试、日志、监控、CI/CD、性能与安全              | 可上线的 AI SaaS 项目   | ⬜   |

## 📐 专项学习计划

- [高等代数 16 周学习计划](roadmap/advanced-algebra.md)：矩阵、向量空间、特征理论、SVD、PCA 与 NumPy 实践

## ✅ 学习清单

### 01 · Python

- [ ] 基础语法、数据结构与异常处理
- [ ] 函数、模块与包管理
- [ ] 面向对象与 `dataclass`
- [ ] 类型标注与静态检查
- [ ] 文件、JSON、日志与配置管理
- [ ] `asyncio` 与异步编程
- [ ] `requests` / HTTP 客户端
- [ ] pandas 数据处理基础
- [ ] pytest 自动化测试

### 02 · Git、Linux 与 Docker

- [ ] clone、commit、push、pull
- [ ] branch、merge、rebase、stash、tag
- [ ] Shell、权限、进程、日志与服务管理
- [ ] grep、find、sed、awk、curl
- [ ] Dockerfile 与镜像优化
- [ ] Docker Compose、Network 与 Volume
- [ ] 容器调试与多服务编排

### 03 · Web 与数据层

- [ ] REST API 与 CRUD
- [ ] FastAPI 路由、依赖注入与校验
- [ ] JWT 认证与权限控制
- [ ] 文件上传、下载与后台任务
- [ ] Streaming 与 WebSocket
- [ ] SQLAlchemy 与 Alembic
- [ ] PostgreSQL 索引、事务与连接池
- [ ] Redis 缓存与基础队列

### 04 · 大模型基础与 API

- [ ] Transformer、Attention、Token、Embedding
- [ ] Context Window、Temperature、Top-p
- [ ] KV Cache、MoE、Fine-tuning、RLHF 基础概念
- [ ] 主流大模型 API 的基本调用
- [ ] 流式响应与多轮对话
- [ ] Structured Outputs 与 JSON Schema
- [ ] Tool / Function Calling
- [ ] 超时、重试、限流与成本控制

### 05 · Prompt Engineering

- [ ] Role 与明确任务边界
- [ ] Zero-shot 与 Few-shot
- [ ] Prompt Template 与变量管理
- [ ] 输出格式与约束设计
- [ ] Prompt Chain 与工作流拆分
- [ ] Prompt 版本管理与评测
- [ ] 注入攻击与数据泄露防护基础

### 06 · RAG

- [ ] PDF、Word、Excel、Markdown、HTML 解析
- [ ] OCR 基础
- [ ] Chunk、Overlap 与语义切分
- [ ] Embedding 模型选择与评估
- [ ] Qdrant、Milvus 或 pgvector
- [ ] Metadata Filter
- [ ] Hybrid Search
- [ ] Re-ranking
- [ ] 引用溯源与检索评测

### 07 · Agent 与 LangGraph

- [ ] State、Node 与 Edge
- [ ] Tool Calling 与工具错误处理
- [ ] Memory 与 Checkpoint
- [ ] Planning 与 Reflection 的适用边界
- [ ] Human in the Loop
- [ ] 可恢复工作流与幂等性
- [ ] 多 Agent 协作基础

### 08 · MCP

- [ ] MCP Server 与 Client
- [ ] Tools
- [ ] Resources
- [ ] Prompts
- [ ] Sampling 基础
- [ ] 权限、输入校验与安全边界
- [ ] 编写并发布一个可复用 MCP Server

### 09 · 前端

- [ ] HTML、CSS、JavaScript 基础
- [ ] TypeScript
- [ ] React 与组件设计
- [ ] Next.js
- [ ] 状态管理
- [ ] 流式聊天界面
- [ ] Markdown 与代码高亮
- [ ] 文件上传、深色模式与移动端适配

### 10 · 模型部署与 AI Infra

- [ ] GPU、CUDA 与显存基础
- [ ] Ollama
- [ ] vLLM
- [ ] SGLang
- [ ] GGUF 与常见量化方案
- [ ] LoRA 基础
- [ ] TensorRT 基础
- [ ] 吞吐、延迟与并发压测

### 11 · 工程质量

- [ ] 单元测试、集成测试与端到端测试
- [ ] 结构化日志与异常追踪
- [ ] OpenTelemetry 基础
- [ ] Prometheus 与 Grafana
- [ ] GitHub Actions CI/CD
- [ ] 配置、密钥与环境隔离
- [ ] 性能、成本、安全与隐私检查

## 🚧 项目规划

### 1. ChatGPT Clone

- [ ] 用户登录与权限控制
- [ ] 多轮对话与历史记录
- [ ] 流式输出与停止生成
- [ ] 多模型切换
- [ ] Markdown、代码高亮与文件上传
- [ ] 深色模式与移动端适配

### 2. 企业知识库（RAG）

- [ ] 多格式文档上传与解析
- [ ] 自动切分、向量化与索引
- [ ] 混合检索、重排与元数据过滤
- [ ] 答案引用与原文定位
- [ ] 会话历史与知识库权限
- [ ] 检索质量评测

### 3. AI 办公助手

- [ ] Word 文档生成
- [ ] Excel 数据分析
- [ ] 日报与会议纪要生成
- [ ] 网页搜索与知识库查询
- [ ] LangGraph 工作流
- [ ] 人工确认后执行关键操作

### 4. MCP 工具平台

- [ ] MCP Server 示例
- [ ] MCP Client 接入
- [ ] Tools、Resources 与 Prompts
- [ ] 工具权限与审计日志
- [ ] 示例文档与调用演示

### 5. AI 代码助手

- [ ] 仓库索引与语义检索
- [ ] 代码问答与引用定位
- [ ] 变更建议与补丁生成
- [ ] 测试执行与结果分析
- [ ] MCP 工具集成

### 6. 多 Agent 协作系统

- [ ] Planner：拆解任务与制定计划
- [ ] Researcher：检索并整理信息
- [ ] Coder：实现与修改代码
- [ ] Reviewer：审查质量与风险
- [ ] Checkpoint、人工审批与失败恢复

### 7. 本地模型服务

- [ ] 部署一个开源大模型
- [ ] 提供兼容的聊天 API
- [ ] 支持流式响应
- [ ] 接入 RAG 或 Agent
- [ ] 完成吞吐与延迟测试

## 🗂️ 仓库结构

```text
.
├── README.md
├── docs/                    # 系统化技术文档
├── notes/                   # 学习与源码阅读笔记
├── roadmap/                 # 月度、周度计划与复盘
├── examples/                # 独立可运行的代码示例
│   ├── python/
│   ├── fastapi/
│   ├── llm-api/
│   ├── rag/
│   └── mcp/
├── projects/                # 完整项目
│   ├── chatbot/
│   ├── enterprise-rag/
│   ├── ai-office/
│   ├── mcp-platform/
│   ├── ai-coding/
│   ├── multi-agent/
│   └── local-model-service/
├── resources/               # 优质资料索引
└── assets/                  # 图片、架构图与演示素材
```

## ⏱️ 学习节奏

### 每周建议

- **理论学习：** 3–5 小时
- **官方文档与源码：** 2–3 小时
- **编码与项目实践：** 7–12 小时
- **测试、复盘与技术输出：** 2–3 小时

### 固定输出

- [ ] 每天至少完成一次有效编码或文档记录
- [ ] 每周完成一个可运行的小功能
- [ ] 每周整理一篇学习总结
- [ ] 每月完成一次阶段复盘
- [ ] 每个阶段交付一个可演示项目

> 兼职投入 10–15 小时/周，可按 9–12 个月执行；全职投入 30–40 小时/周，可压缩至约 4–6 个月。

## 📦 项目交付标准

每个作品集项目至少应包含：

- [ ] 清晰的 README 与功能说明
- [ ] 架构图和关键技术决策
- [ ] 环境变量示例（不得提交真实密钥）
- [ ] 一键启动方式或 Docker Compose
- [ ] API 文档
- [ ] 自动化测试
- [ ] 演示截图或视频
- [ ] 已知限制与后续计划
- [ ] 版本迭代记录

## 📚 推荐资源

学习时优先阅读官方文档，并结合源码和项目实践验证。

### 编程与后端

- [Python Documentation](https://docs.python.org/3/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Docker Documentation](https://docs.docker.com/)

### AI 应用开发

- [OpenAI Platform Documentation](https://platform.openai.com/docs/)
- [Anthropic Documentation](https://docs.anthropic.com/)
- [Google AI for Developers](https://ai.google.dev/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Model Context Protocol](https://modelcontextprotocol.io/)

### 检索与模型部署

- [Qdrant Documentation](https://qdrant.tech/documentation/)
- [Milvus Documentation](https://milvus.io/docs/)
- [pgvector](https://github.com/pgvector/pgvector)
- [Ollama Documentation](https://docs.ollama.com/)
- [vLLM Documentation](https://docs.vllm.ai/)
- [SGLang Documentation](https://docs.sglang.ai/)

### 推荐阅读的开源项目

- [FastAPI](https://github.com/fastapi/fastapi)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LlamaIndex](https://github.com/run-llama/llama_index)
- [Open WebUI](https://github.com/open-webui/open-webui)
- [Qdrant](https://github.com/qdrant/qdrant)
- [vLLM](https://github.com/vllm-project/vllm)
- [OpenHands](https://github.com/All-Hands-AI/OpenHands)

## 🏁 最终目标

完成本路线后，我希望能够：

- 从零搭建并上线一个完整的 AI Web 应用
- 合理选择和接入不同大模型
- 设计具有引用、权限和评测能力的 RAG 系统
- 开发可恢复、可观测、有人类监督的 Agent 工作流
- 编写 MCP Server 与 Client，并安全接入外部工具
- 使用 Docker 部署应用和本地模型服务
- 编写测试、CI/CD、日志与监控配置
- 阅读并贡献优秀开源项目
- 用真实项目证明工程能力与产品思维

## 🤝 参与交流

欢迎通过 Issue 分享建议、学习资料和实践经验。如果这个仓库对你有所帮助，欢迎 Star ⭐。

> **Learning in Public · Build in Public · Grow in Public**

## 📄 License

本仓库中的原创文档默认采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)；示例代码可根据仓库实际需要另行添加 MIT License。发布前请在根目录补充对应的 `LICENSE` 文件。
