# 如何在新项目中使用 Ralph Loop

## 🚀 快速开始（3 步）

### 步骤 1: 创建项目

```bash
mkdir ~/my-new-project
cd ~/my-new-project
```

### 步骤 2: 启动 Ralph Loop

```bash
ralph-loop "创建一个 Python Flask API，包含用户增删改查接口"
```

### 步骤 3: 等待完成

Ralph Loop 会自动：
- 创建文件
- 编写代码
- 运行测试
- 迭代改进

---

## 📖 详细指南

### 方式 1: 全局命令（推荐）⭐

**适用场景**: 任何新项目

```bash
# 基本用法
ralph-loop "你的任务描述"

# 自定义迭代次数
ralph-loop "优化数据库查询" 15

# 自定义完成承诺
ralph-loop "添加测试" 20 "TESTS_DONE"
```

**优点**:
- ✅ 随时随地可用
- ✅ 无需额外配置
- ✅ 命令简洁

---

### 方式 2: 通过 AI 助手

**适用场景**: 需要更多控制或解释

```
请使用 ralph-loop 技能，帮我创建一个用户认证系统
```

或者更详细：

```
启动 Ralph Loop，任务是"重构 API 层代码"，
最大迭代 15 次，完成承诺是 "REFACTOR_COMPLETE"
```

**优点**:
- ✅ 可以对话式调整
- ✅ AI 可以解释每个步骤
- ✅ 适合复杂任务

---

### 方式 3: 项目启动脚本

**适用场景**: 需要项目特定的配置

```bash
# 1. 复制启动脚本
cp ~/RalphLoop/start-ralph-loop.sh ./start-ralph-loop.sh

# 2. 修改默认参数（可选）
nano start-ralph-loop.sh

# 3. 使用
./start-ralph-loop.sh "你的任务"
```

**优点**:
- ✅ 可自定义默认值
- ✅ 可添加项目特定配置
- ✅ 版本控制友好

---

## 💡 实战示例

### 示例 1: 创建 FastAPI 项目

```bash
mkdir ~/fastapi-demo
cd ~/fastapi-demo

ralph-loop "创建一个 FastAPI 项目，包含用户 CRUD 接口和数据库模型"
```

**预期产出**:
- `main.py` - FastAPI 应用
- `models.py` - 数据模型
- `requirements.txt` - 依赖文件
- 基本的 API 文档

---

### 示例 2: 添加测试覆盖

```bash
cd ~/existing-project

ralph-loop "为所有 Python 函数添加单元测试" 15 "ALL_TESTS_PASS"
```

**预期产出**:
- `test_*.py` - 测试文件
- 高测试覆盖率
- 所有测试通过

---

### 示例 3: 代码重构

```bash
cd ~/legacy-project

ralph-loop "将所有 callback 重构为 async/await" 20 "REFACTOR_COMPLETE"
```

**预期产出**:
- 现代化的异步代码
- 保持功能不变
- 性能优化

---

## 🎯 任务描述技巧

### ❌ 不好的描述

```bash
# 太模糊
ralph-loop "改进代码"

# 太宽泛
ralph-loop "做一个网站"

# 不明确
ralph-loop "优化"
```

### ✅ 好的描述

```bash
# 具体
ralph-loop "创建一个 Flask RESTful API，包含用户增删改查接口"

# 可验证
ralph-loop "添加单元测试，覆盖率达到 80%"

# 明确边界
ralph-loop "将 src/ 目录下的所有 var 替换为 const/let"
```

---

## 🔧 循环管理

### 查看循环状态

```bash
# 查看完整状态
cat .claude/ralph-loop.local.md

# 只看迭代次数
grep '^iteration:' .claude/ralph-loop.local.md

# 查看任务描述
grep '^prompt:' .claude/ralph-loop.local.md
```

### 停止循环

```bash
# 手动停止
rm .claude/ralph-loop.local.md

# 验证已停止
ls .claude/ralph-loop.local.md
# ls: cannot access '.claude/ralph-loop.local.md': No such file or directory
```

---

## ⚙️ 参数说明

### 基本格式

```bash
ralph-loop "任务描述" [最大迭代] [完成承诺]
```

### 参数详解

1. **任务描述**（必需）
   - 要完成的工作
   - 建议用引号括起来
   - 要具体明确

2. **最大迭代**（可选，默认 10）
   - 数字，0 表示无限
   - 建议: 5-25
   - 防止无限循环

3. **完成承诺**（可选，默认 CALCULATOR_DONE）
   - 任务完成时输出的文本
   - 必须完全匹配
   - 格式: `<promise>文本</promise>`

---

## 📊 迭代次数建议

| 任务复杂度 | 建议迭代次数 | 示例 |
|-----------|-------------|------|
| 简单 | 5-10 | 添加一个函数 |
| 中等 | 10-15 | 创建模块 |
| 复杂 | 15-25 | 重构架构 |
| 超复杂 | 25-50 | 新功能开发 |

---

## ⚠️ 常见问题

### Q1: Ralph Loop 不停止怎么办？

**A**: 手动停止

```bash
rm .claude/ralph-loop.local.md
```

### Q2: 如何查看当前进度？

**A**: 查看状态文件

```bash
cat .claude/ralph-loop.local.md
```

### Q3: 可以同时运行多个循环吗？

**A**: 不建议。每个项目一次只能运行一个循环。

### Q4: 任务太复杂怎么办？

**A**: 拆分成多个小任务

```bash
ralph-loop "创建基础架构" 10 "PHASE_1_DONE"
ralph-loop "添加认证功能" 10 "PHASE_2_DONE"
ralph-loop "添加业务逻辑" 10 "PHASE_3_DONE"
```

### Q5: Promise 检测失败怎么办？

**A**: 使用手动停止或设置最大迭代

```bash
# 方式 1: 设置最大迭代
ralph-loop "任务" 15

# 方式 2: 手动停止
rm .claude/ralph-loop.local.md
```

---

## 🎓 学习路径

### 初学者

1. 阅读 `~/RalphLoop/QUICK_START.md`
2. 尝试简单任务
3. 观察迭代过程
4. 理解工作原理

### 进阶用户

1. 阅读 `~/RalphLoop/CASE_STUDY.md`
2. 尝试中等复杂度任务
3. 学习任务分解
4. 优化迭代次数

### 高级用户

1. 自定义启动脚本
2. 集成到工作流
3. 创建项目模板
4. 分享最佳实践

---

## 🚀 准备好了吗？

在新项目中尝试：

```bash
# 创建测试项目
mkdir ~/test-ralph-loop
cd ~/test-ralph-loop

# 启动第一个循环
ralph-loop "创建一个简单的 Hello World Python 脚本，包含错误处理"

# 观察魔法发生！
```

---

## 📚 相关资源

- **完整案例**: `~/RalphLoop/CASE_STUDY.md`
- **快速指南**: `~/RalphLoop/QUICK_START.md`
- **使用示例**: `~/RalphLoop/USAGE_EXAMPLES.md`
- **全局使用**: `~/RalphLoop/RALPH_LOOP_GLOBAL_USAGE.md`

---

**提示**: Ralph Loop 最适合有明确完成标准的任务。开始前先想清楚目标，会让迭代更有效率！
