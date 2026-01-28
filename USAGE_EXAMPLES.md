# Ralph Loop 简化启动脚本使用指南

## 🚀 超简单使用方式

### 基本用法（只需提供任务）

```bash
./start-ralph-loop.sh "创建一个支持加减乘除的 Python 计算器"
```

自动使用：
- 最大迭代：**10 次**
- 完成承诺：**CALCULATOR_DONE**

---

## 📋 更多示例

### 示例 1: 创建计算器
```bash
./start-ralph-loop.sh "创建一个支持加减乘除的 Python 计算器"
```

### 示例 2: 修复 Bug
```bash
./start-ralph-loop.sh "修复登录功能的认证 bug"
```

### 示例 3: 重构代码
```bash
./start-ralph-loop.sh "将所有 var 替换为 const/let"
```

### 示例 4: 添加测试
```bash
./start-ralph-loop.sh "为所有函数添加单元测试"
```

### 示例 5: 自定义参数
```bash
./start-ralph-loop.sh "优化 API 性能" 20 "OPTIMIZED"
```

---

## ⚙️ 自定义参数

如果需要自定义参数，可以添加：

```bash
./start-ralph-loop.sh "任务描述" [最大迭代次数] [完成承诺]
```

### 示例：
```bash
# 15 次迭代，自定义承诺
./start-ralph-loop.sh "重构代码" 15 "REFACTOR_COMPLETE"

# 无限迭代，自定义承诺
./start-ralph-loop.sh "持续改进代码" 0 "IMPROVED"

# 使用默认承诺，自定义迭代次数
./start-ralph-loop.sh "添加测试" 20
```

---

## 📊 输出说明

运行脚本后，你会看到：

```
🚀 启动 Ralph Loop...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 任务: 创建一个 Python 计算器
🔄 最大迭代: 10
✅ 完成承诺: CALCULATOR_DONE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

然后 Claude 会开始迭代工作，直到：
1. 检测到 `<promise>CALCULATOR_DONE</promise>`
2. 达到 10 次迭代
3. 手动取消（`rm .claude/ralph-loop.local.md`）

---

## 💡 最佳实践

### ✅ DO - 推荐做法

1. **任务描述要具体**
   ```bash
   ./start-ralph-loop.sh "创建 Python 计算器，支持加减乘除，包含错误处理和单元测试"
   ```

2. **合理设置迭代次数**
   ```bash
   ./start-ralph-loop.sh "简单任务" 5      # 简单任务用较少迭代
   ./start-ralph-loop.sh "复杂任务" 20     # 复杂任务用更多迭代
   ```

3. **使用有意义的承诺**
   ```bash
   ./start-ralph-loop.sh "修复 bug" 10 "ALL_TESTS_PASS"
   ./start-ralph-loop.sh "添加功能" 15 "FEATURE_COMPLETE"
   ```

### ❌ DON'T - 避免做法

1. 不要使用模糊的任务描述
   ```bash
   ❌ ./start-ralph-loop.sh "改进代码"
   ✅ ./start-ralph-loop.sh "将 var 替换为 const/let"
   ```

2. 不要设置过大的迭代次数
   ```bash
   ❌ ./start-ralph-loop.sh "任务" 1000
   ✅ ./start-ralph-loop.sh "任务" 20
   ```

---

## 🛠️ 管理循环

### 查看当前状态
```bash
cat .claude/ralph-loop.local.md
```

### 查看迭代次数
```bash
grep '^iteration:' .claude/ralph-loop.local.md
```

### 取消循环
```bash
rm .claude/ralph-loop.local.md
```

---

## 🎯 完整工作流程示例

```bash
# 1. 启动循环
./start-ralph-loop.sh "创建 Python 计算器"

# 2. Claude 开始工作...

# 3. 检查进度（另一个终端）
cat .claude/ralph-loop.local.md

# 4. 如果需要取消
rm .claude/ralph-loop.local.md

# 5. 查看完成的工作
ls -la
```

---

## 📝 默认设置说明

**为什么默认值是 10 和 CALCULATOR_DONE？**

- **10 次迭代**：适合大多数任务的合理迭代次数
  - 足够时间迭代改进
  - 不会无限循环
  - 可根据需要调整

- **CALCULATOR_DONE**：只是一个示例
  - 实际使用时会根据任务自动调整
  - 可以通过第三个参数自定义

---

## ✨ 快速开始

现在就试试：

```bash
./start-ralph-loop.sh "创建一个简单的 Hello World 程序"
```

就这么简单！🎉
