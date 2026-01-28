# Ralph Loop 快速开始指南

## 🚀 快速测试命令

### 1. 查看帮助
```bash
/ralph-wiggum:help
```

### 2. 启动一个简单的迭代任务
```bash
/ralph-loop "创建一个 Python 计算器，支持加减乘除运算，并添加单元测试。完成后输出 <promise>CALCULATOR_DONE</promise>" --completion-promise "CALCULATOR_DONE" --max-iterations 5
```

### 3. 取消当前循环
```bash
/cancel-ralph
```

## 📝 实际使用示例

### 示例 1: 代码重构
```bash
/ralph-loop "重构 app.js 中的 API 调用代码，使用 async/await 替代回调函数，确保所有测试通过。完成后输出 <promise>REFACTOR_COMPLETE</promise>" --completion-promise "REFACTOR_COMPLETE" --max-iterations 10
```

### 示例 2: 添加测试
```bash
/ralph-loop "为 utils.py 中的所有函数添加单元测试，覆盖率要求达到 80%。完成后输出 <promise>TESTS_ADDED</promise>" --completion-promise "TESTS_ADDED" --max-iterations 8
```

### 示例 3: Bug 修复
```bash
/ralph-loop "修复 login 函数中的认证 bug，运行所有相关测试确保修复成功。完成后输出 <promise>BUG_FIXED</promise>" --completion-promise "BUG_FIXED" --max-iterations 15
```

## 🔍 监控循环状态

### 查看当前循环状态
```bash
cat .claude/.ralph-loop.local.md
```

### 检查迭代次数
```bash
grep '^iteration:' .claude/.ralph-loop.local.md
```

### 检查完成承诺
```bash
grep '^completion_promise:' .claude/.ralph-loop.local.md
```

## ⚙️ 工作原理

1. **启动**: 创建 `.claude/.ralph-loop.local.md` 状态文件
2. **工作**: Claude 执行任务，修改代码
3. **拦截**: Exit 时 stop hook 拦截退出
4. **检查**: 检测是否输出 `<promise>...</promise>`
5. **循环**: 如果未完成，重新注入相同 prompt
6. **完成**: 检测到 promise 或达到最大迭代次数

## 💡 最佳实践

### ✅ DO - 推荐做法

1. **明确的任务描述**
   ```
   ✅ "将所有 var 替换为 const/let，确保代码仍可运行"
   ❌ "改进代码质量"
   ```

2. **可验证的完成条件**
   ```
   ✅ "所有测试通过，输出 <promise>TESTS_PASS</promise>"
   ❌ "代码看起来不错"
   ```

3. **合理的迭代限制**
   ```
   ✅ --max-iterations 10
   ❌ --max-iterations 1000
   ```

4. **具体的成功指标**
   ```
   ✅ "测试覆盖率达到 75%，所有测试通过"
   ❌ "添加一些测试"
   ```

### ❌ DON'T - 避免做法

1. 不要过早输出 `<promise>` - 必须确保任务真正完成
2. 不要设置过大的 max-iterations - 会导致无限循环
3. 不要使用模糊的任务描述 - 会导致不可预测的结果
4. 不要在生产环境紧急情况使用 - 适合开发迭代，不适合救火

## 🎯 适用场景矩阵

| 场景 | 适用性 | 理由 |
|------|--------|------|
| 代码重构 | ⭐⭐⭐⭐⭐ | 需要多轮迭代和测试验证 |
| 添加测试 | ⭐⭐⭐⭐⭐ | 有明确的覆盖率目标 |
| Bug 修复 | ⭐⭐⭐⭐ | 可通过测试验证修复 |
| 功能开发 | ⭐⭐⭐⭐ | 渐进式开发很合适 |
| 代码审查 | ⭐⭐ | 需要人工判断 |
| 架构设计 | ⭐⭐ | 需要人类决策 |
| 文档编写 | ⭐⭐⭐ | 可以迭代改进 |
| 性能优化 | ⭐⭐⭐⭐ | 可通过基准测试验证 |

## 🛠️ 故障排除

### 问题: 循环没有停止
**解决方案**: 使用 `/cancel-ralph` 手动停止

### 问题: 任务没有进展
**解决方案**:
1. 检查任务描述是否清晰
2. 减小 max-iterations
3. 手动干预后重启循环

### 问题: Promise 不被识别
**解决方案**:
1. 确保使用 XML 标签: `<promise>TEXT</promise>`
2. Promise 文本必须与设置的一致
3. Promise 内容必须全部大写

## 📚 更多资源

- 详细文档: `/ralph-wiggum:help`
- 完整测试报告: `TEST_REPORT.md`
- 原始技术: https://ghuntley.com/ralph/
