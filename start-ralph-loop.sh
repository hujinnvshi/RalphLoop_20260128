#!/bin/bash
# Ralph Loop 快速启动脚本

RALPH_SCRIPT=$(find ~/.claude/plugins/cache -path "*/ralph-wiggum/*/scripts/setup-ralph-loop.sh" 2>/dev/null | head -1)

if [ -z "$RALPH_SCRIPT" ]; then
    echo "❌ Ralph Wiggum 插件未找到"
    echo "   请确保插件已正确安装"
    exit 1
fi

if [ $# -lt 1 ]; then
    echo "📖 Ralph Loop 启动脚本（简化版）"
    echo ""
    echo "用法: $0 \"任务描述\""
    echo ""
    echo "默认设置:"
    echo "  • 最大迭代: 10 次"
    echo "  • 完成承诺: CALCULATOR_DONE"
    echo ""
    echo "可选参数:"
    echo "  $0 \"任务描述\" [最大迭代] [完成承诺]"
    echo ""
    echo "示例:"
    echo "  $0 \"创建一个 Python 计算器\""
    echo "  $0 \"修复所有 bug\""
    echo "  $0 \"重构代码\" 15 \"REFACTOR_COMPLETE\""
    echo ""
    exit 1
fi

PROMPT="$1"
MAX_ITER="${2:-10}"
PROMISE="${3:-CALCULATOR_DONE}"

ARGS=("$PROMPT")
if [ "$MAX_ITER" -gt 0 ]; then
    ARGS+=("--max-iterations" "$MAX_ITER")
fi
if [ -n "$PROMISE" ]; then
    ARGS+=("--completion-promise" "$PROMISE")
fi

echo "🚀 启动 Ralph Loop..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📝 任务: $PROMPT"
echo "🔄 最大迭代: $MAX_ITER"
if [ -n "$PROMISE" ]; then
    echo "✅ 完成承诺: $PROMISE"
fi
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

"$RALPH_SCRIPT" "${ARGS[@]}"
