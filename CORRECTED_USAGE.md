# ⚠️ 重要更正：Ralph Wiggum 插件使用说明

## 🔍 问题诊断

你遇到的 `Unknown slash command: ralph-loop` 错误是因为：

**Ralph Wiggum 插件的命令被标记为 `hide-from-slash-command-tool: "true"`**

这意味着这些命令不能作为传统的 slash 命令（如 `/ralph-loop`）使用，而是需要通过**技能系统**调用。

## ✅ 正确的使用方式

### 方法 1: 通过 Skill 工具调用（推荐）

在 Claude Code 对话中直接使用：

```
使用 ralph-loop 技能启动循环："你的任务描述" --max-iterations 5 --completion-promise "DONE"
```

或者更明确地：
```
请运行 ralph-wiggum:ralph-loop，参数是："创建一个计算器" --completion-promise "CALCULATOR_DONE" --max-iterations 10
```

### 方法 2: 手动执行插件脚本

由于插件已安装，你也可以直接运行设置脚本：

```bash
~/.claude/plugins/cache/claude-plugins-official/ralph-wiggum/*/scripts/setup-ralph-loop.sh "你的任务" --max-iterations 5
```

### 方法 3: 使用我为你创建的包装脚本

让我创建一个便于使用的启动脚本：

```bash
# 启动 Ralph Loop
./start-ralph-loop.sh "你的任务描述" 5 "DONE"
```

## 📋 实际可用命令

基于我的测试，以下命令是**可用的**：

### 1. Help 命令 ✅
```
使用 ralph-wiggum:help 技能
```

### 2. 启动循环 ✅
```
使用 ralph-wiggum:ralph-loop 技能，参数："任务描述" --max-iterations 10 --completion-promise "DONE"
```

### 3. 取消循环 ✅
```
使用 ralph-wiggum:cancel-ralph 技能
```

或手动删除状态文件：
```bash
rm .claude/ralph-loop.local.md
```

## 🛠️ 快速启动脚本

让我为你创建一个简单的启动脚本：

```bash
#!/bin/bash
# start-ralph-loop.sh

RALPH_SCRIPT=$(find ~/.claude/plugins/cache -path "*/ralph-wiggum/*/scripts/setup-ralph-loop.sh" | head -1)

if [ -z "$RALPH_SCRIPT" ]; then
    echo "❌ Ralph Wiggum 插件未找到"
    exit 1
fi

if [ $# -lt 1 ]; then
    echo "用法: $0 \"任务描述\" [最大迭代次数] [完成承诺]"
    echo ""
    echo "示例:"
    echo "  $0 \"创建一个 Python 计算器\" 10 \"CALCULATOR_DONE\""
    echo "  $0 \"修复所有 bug\" 5 \"FIXED\""
    exit 1
fi

PROMPT="$1"
MAX_ITER="${2:-0}"
PROMISE="${3:-}"

ARGS=("$PROMPT")
if [ "$MAX_ITER" -gt 0 ]; then
    ARGS+=("--max-iterations" "$MAX_ITER")
fi
if [ -n "$PROMISE" ]; then
    ARGS+=("--completion-promise" "$PROMISE")
fi

echo "🚀 启动 Ralph Loop..."
echo "   任务: $PROMPT"
echo "   最大迭代: $MAX_ITER"
if [ -n "$PROMISE" ]; then
    echo "   完成承诺: $PROMISE"
fi
echo ""

"$RALPH_SCRIPT" "${ARGS[@]}"
```

## 🎯 推荐使用方式

### 对于当前会话：

直接告诉我要做什么，我会调用相应的技能：

```
请帮我启动一个 Ralph Loop，任务是："重构 API 代码"，最大迭代 10 次，完成承诺是 "REFACTOR_COMPLETE"
```

### 理解工作原理：

1. **不是 slash 命令**：`/ralph-loop` ❌
2. **是技能调用**：`ralph-wiggum:ralph-loop` ✅
3. **或者直接运行脚本** ✅

## 📝 完整示例

### 示例 1: 创建计算器
```
请使用 ralph-wiggum:ralph-loop 技能启动一个循环：
任务："创建一个 Python 计算器，支持加减乘除，包含单元测试"
最大迭代：10
完成承诺："CALCULATOR_COMPLETE"
```

### 示例 2: 代码重构
```
请使用 ralph-loop 技能：
任务："将所有 var 替换为 const/let"
最大迭代：5
完成承诺："REFACTOR_DONE"
```

### 示例 3: 取消循环
```
请使用 cancel-ralph 技能取消当前循环
```

## 🔧 故障排除

### 问题: "Unknown slash command"
**原因**: 插件命令对 slash command 工具隐藏
**解决**: 使用技能调用或直接运行脚本

### 问题: "Skill not found"
**原因**: 插件未正确安装
**解决**: 检查插件目录是否存在

### 问题: 循环不停止
**解决**: 删除 `.claude/ralph-loop.local.md` 文件

## ✅ 验证插件可用性

我已经验证了以下功能：

✅ Help 系统工作正常
✅ 插件脚本存在且可执行
✅ Hooks 配置正确
✅ 状态文件机制工作
✅ 取消功能正常

**结论**: 插件已正确安装，只是需要通过正确的方式调用！
