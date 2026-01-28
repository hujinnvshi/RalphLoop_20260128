# Ralph Loop 全局启动器使用指南

## ✅ 已配置完成

Ralph Loop 启动脚本已成功配置为全局可用！

## 🚀 快速使用

### 基本用法

在任何项目/目录中直接运行：

```bash
ralph-loop "你的任务描述"
```

### 自定义参数

```bash
# 自定义迭代次数
ralph-loop "优化数据库查询" 15

# 自定义完成承诺
ralph-loop "添加测试" 20 "TESTS_DONE"

# 完全自定义
ralph-loop "重构代码" 25 "REFACTOR_COMPLETE"
```

## 📍 可用的版本

### 1. 全局命令（推荐）
```bash
ralph-loop "任务"
```
- 位置: `/usr/local/bin/ralph-loop`
- 可用性: 任何目录
- 需求: 无

### 2. 用户级脚本
```bash
~/ralph-loop.sh "任务"
```
- 位置: `~/ralph-loop.sh`
- 可用性: 任何目录
- 需求: 无

### 3. 项目本地脚本
```bash
./start-ralph-loop.sh "任务"
```
- 位置: 项目目录
- 可用性: 仅当前项目
- 需求: 需复制到项目

## 🎯 为什么可以全局复用？

### 技术原理

1. **动态路径查找**
   ```bash
   RALPH_SCRIPT=$(find ~/.claude/plugins/cache -path "*/ralph-wiggum/*/scripts/setup-ralph-loop.sh")
   ```
   - 自动查找 Ralph Wiggum 插件位置
   - 不依赖硬编码路径

2. **插件位置全局化**
   - Claude Code 插件安装在 `~/.claude/plugins/`
   - 这个位置对所有项目都是固定的

3. **无项目依赖**
   - 不需要特定项目文件
   - 不需要特定目录结构
   - 可以在任何地方运行

## 💡 使用场景

### 场景 1: 快速原型开发

```bash
cd ~/projects/new-api
ralph-loop "创建一个 RESTful API，使用 Flask 和 SQLAlchemy"
```

### 场景 2: 代码重构

```bash
cd ~/legacy-project
ralph-loop "将所有 callback 改为 async/await" 15 "REFACTOR_DONE"
```

### 场景 3: 测试生成

```bash
cd ~/my-project
ralph-loop "为所有函数添加单元测试" 20 "TESTS_COMPLETE"
```

### 场景 4: Bug 修复

```bash
cd ~/bug-project
ralph-loop "修复登录页面的认证问题" 10 "FIXED"
```

## 🔧 配置管理

### 检查全局安装

```bash
which ralph-loop
# 输出: /usr/local/bin/ralph-loop
```

### 查看脚本内容

```bash
cat ~/ralph-loop.sh
# 或
cat /usr/local/bin/ralph-loop
```

### 更新全局脚本

如果需要修改脚本：

```bash
# 1. 编辑用户级版本
nano ~/ralph-loop.sh

# 2. 重新安装到全局
sudo cp ~/ralph-loop.sh /usr/local/bin/ralph-loop
```

### 卸载全局命令

```bash
sudo rm /usr/local/bin/ralph-loop
```

## 📋 参数说明

### 必需参数

- **任务描述**: 要完成的任务，建议用引号括起来

### 可选参数

- **最大迭代次数**: 数字，默认 10
  - `0` = 无限循环（不推荐）
  - `5-20` = 推荐范围

- **完成承诺**: 文本，默认 "CALCULATOR_DONE"
  - 当任务完成时必须输出此文本
  - 格式: `<promise>你的承诺</promise>`

## ⚠️ 注意事项

### 1. 任务描述要清晰

❌ 不好的描述:
```bash
ralph-loop "改进代码"
```

✅ 好的描述:
```bash
ralph-loop "将所有 var 替换为 const/let，确保代码仍可运行"
```

### 2. 设置合理的迭代次数

```bash
# 简单任务
ralph-loop "修复 typo" 5

# 中等任务
ralph-loop "添加错误处理" 10

# 复杂任务
ralph-loop "重构架构" 20
```

### 3. 使用有意义的完成承诺

```bash
# 清晰的承诺
ralph-loop "添加测试" 10 "ALL_TESTS_PASS"

# 具体的承诺
ralph-loop "实现功能" 15 "FEATURE_READY"
```

### 4. 监控循环状态

```bash
# 查看当前循环
cat .claude/ralph-loop.local.md

# 查看迭代次数
grep '^iteration:' .claude/ralph-loop.local.md

# 取消循环
rm .claude/ralph-loop.local.md
```

## 🎓 最佳实践

### 1. 明确的任务定义

```bash
# ✅ 好：具体、可验证
ralph-loop "实现用户登录功能，包含邮箱验证，测试覆盖率 80%"

# ❌ 差：模糊、难以验证
ralph-loop "做个登录功能"
```

### 2. 合理的迭代预期

```bash
# 简单任务：5-10 次
ralph-loop "添加 README 文档" 5

# 中等任务：10-15 次
ralph-loop "添加错误处理" 10

# 复杂任务：15-25 次
ralph-loop "重构数据层" 20
```

### 3. 验证驱动

```bash
# 包含验证标准
ralph-loop "实现缓存，所有 API 响应时间 < 100ms" 15 "PERFORMANCE_OK"
```

### 4. 渐进式开发

```bash
# 拆分大任务
ralph-loop "实现 API 基础框架" 10 "FRAMEWORK_DONE"
ralph-loop "添加认证功能" 10 "AUTH_DONE"
ralph-loop "添加数据验证" 10 "VALIDATION_DONE"
```

## 🐛 故障排除

### 问题: 命令找不到

```bash
# 检查是否安装
which ralph-loop

# 如果没有输出，重新安装
sudo cp ~/ralph-loop.sh /usr/local/bin/ralph-loop
```

### 问题: 插件未找到

```bash
# 检查插件是否存在
ls ~/.claude/plugins/cache/claude-plugins-official/ralph-wiggum/

# 如果不存在，重新安装 Ralph Wiggum 插件
```

### 问题: 循环不停止

```bash
# 手动取消
rm .claude/ralph-loop.local.md

# 或者设置合理的最大迭代次数
ralph-loop "任务" 10 "DONE"
```

## 📚 相关资源

- Ralph Wiggum 原始技术: https://ghuntley.com/ralph/
- 插件帮助: `/ralph-wiggum:help`
- 项目文档: `README.md`

## ✨ 总结

Ralph Loop 启动脚本：

- ✅ **全局可用**: 在任何目录都可以使用
- ✅ **易于使用**: 简单的命令格式
- ✅ **高度可复用**: 不依赖特定项目
- ✅ **灵活配置**: 支持多种参数组合

现在你可以在任何项目中享受 Ralph Loop 的强大功能了！
