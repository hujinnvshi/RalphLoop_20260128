#!/bin/bash
# 启动 HTTPS 计算器服务器

echo "=========================================="
echo "  Python 计算器 Web 服务 (HTTPS)"
echo "=========================================="
echo ""
echo "服务器地址: https://172.16.48.112:15032"
echo ""
echo "按 Ctrl+C 停止服务器"
echo ""
echo "=========================================="
echo ""

# 检查证书文件
if [ ! -f "certs/cert.pem" ] || [ ! -f "certs/key.pem" ]; then
    echo "❌ 错误: 证书文件不存在"
    echo "   请运行: mkdir -p certs && openssl req -x509 -newkey rsa:4096 -nodes \\"
    echo "     -out certs/cert.pem -keyout certs/key.pem -days 365 \\"
    echo "     -subj \"/C=CN/ST=State/L=City/O=Organization/CN=172.16.48.112\""
    exit 1
fi

# 启动应用
python3 app.py
