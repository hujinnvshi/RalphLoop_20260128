# HTTPS 配置说明

## 配置信息

- **服务器地址**: `172.16.48.112`
- **端口**: `15032`
- **协议**: HTTPS (SSL/TLS)
- **证书类型**: 自签名证书

## 快速启动

### 1. 启动 HTTPS 服务器

```bash
./start-https.sh
```

### 2. 访问 Web 界面

在浏览器中打开:
```
https://172.16.48.112:15032
```

⚠️ **重要**: 浏览器会显示"不安全"警告，这是因为使用的是自签名证书。这是正常的！

### 3. 在浏览器中接受证书

- Chrome: 点击"高级" → "继续访问"
- Firefox: 点击"高级" → "接受风险并继续"
- Safari: 点击"详细信息" → "访问此网站"

## 配置测试

### 运行配置测试

```bash
python3 test_https_config.py
```

这将验证：
- ✓ 证书文件存在
- ✓ 证书有效性
- ✓ 端口配置正确
- ✓ 应用配置正确

## 证书信息

### 证书详情

- **颁发给**: 172.16.48.112
- **颁发者**: Self-signed
- **有效期**: 365 天
- **加密算法**: RSA 4096
- **证书文件**: `certs/cert.pem`
- **私钥文件**: `certs/key.pem`

### 重新生成证书

如果需要重新生成证书：

```bash
mkdir -p certs
openssl req -x509 -newkey rsa:4096 -nodes \
  -out certs/cert.pem \
  -keyout certs/key.pem \
  -days 365 \
  -subj "/C=CN/ST=State/L=City/O=Organization/CN=172.16.48.112"
```

## 配置文件

### app.py 关键配置

```python
if __name__ == '__main__':
    # SSL 上下文配置
    context = ('certs/cert.pem', 'certs/key.pem')

    # 运行 HTTPS 服务器
    app.run(
        debug=True,
        host='172.16.48.112',
        port=15032,
        ssl_context=context
    )
```

## 网络配置

### 防火墙设置

确保端口 15032 已开放：

```bash
# Ubuntu/Debian
sudo ufw allow 15032/tcp

# CentOS/RHEL
sudo firewall-cmd --add-port=15032/tcp --permanent
sudo firewall-cmd --reload
```

### 检查端口监听

```bash
# 检查端口是否在监听
netstat -tuln | grep 15032

# 或使用 ss
ss -tuln | grep 15032
```

## 测试 HTTPS 连接

### 使用 curl 测试（忽略证书验证）

```bash
curl -k https://172.16.48.112:15032/api/health
```

预期响应：
```json
{"status": "ok", "service": "calculator"}
```

### 使用 Python 测试

```python
import requests
import urllib3

# 禁用 SSL 警告（仅用于测试）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 测试 API
response = requests.get('https://172.16.48.112:15032/api/health', verify=False)
print(response.json())
```

## 安全说明

### 自签名证书的特点

✅ **优点**:
- 免费
- 快速生成
- 适合开发/测试环境
- 提供加密功能

⚠️ **缺点**:
- 浏览器不信任（显示警告）
- 无法验证服务器身份
- 不适合生产环境

### 生产环境建议

对于生产环境，建议使用：

1. **Let's Encrypt** (免费)
   ```bash
   sudo apt-get install certbot
   sudo certbot certonly --standalone -d yourdomain.com
   ```

2. **商业证书**
   - DigiCert
   - Comodo
   - GlobalSign

3. **云服务证书**
   - AWS Certificate Manager
   - Azure App Service Certificates
   - Google Cloud Certificate Manager

## 故障排除

### 问题 1: 无法绑定到 172.16.48.112

**原因**: IP 地址不可用

**解决**:
```bash
# 检查 IP 地址
ip addr show | grep 172.16.48.112

# 或使用 0.0.0.0（所有接口）
# 修改 app.py 中的 host 为 '0.0.0.0'
```

### 问题 2: 端口已被占用

**原因**: 端口 15032 已被其他程序使用

**解决**:
```bash
# 查找占用端口的进程
sudo lsof -i :15032

# 杀死进程
sudo kill -9 <PID>

# 或修改为其他端口
```

### 问题 3: 证书文件找不到

**原因**: 证书路径不正确

**解决**:
```bash
# 确认证书文件存在
ls -lh certs/cert.pem certs/key.pem

# 重新生成证书
mkdir -p certs
openssl req -x509 -newkey rsa:4096 -nodes \
  -out certs/cert.pem \
  -keyout certs/key.pem \
  -days 365 \
  -subj "/C=CN/ST=State/L=City/O=Organization/CN=172.16.48.112"
```

### 问题 4: 浏览器显示"连接不安全"

**原因**: 自签名证书不受信任

**解决**: 这是正常的！点击"高级"→"继续访问"即可。

## 配置验证清单

- [ ] 证书文件已生成 (`certs/cert.pem`, `certs/key.pem`)
- [ ] app.py 已更新（host 和 port）
- [ ] SSL 上下文已配置
- [ ] 配置测试通过 (`python3 test_https_config.py`)
- [ ] 防火墙端口已开放
- [ ] 服务器可成功启动
- [ ] 浏览器可以访问（接受警告后）

## API 使用示例

### HTTPS API 调用

```bash
# 计算请求
curl -k -X POST https://172.16.48.112:15032/calculate \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 5, "operator": "+"}'
```

响应:
```json
{
  "success": true,
  "result": 15,
  "expression": "10.0 + 5.0"
}
```

## 更多信息

- 查看完整文档: `README.md`
- 运行测试: `python3 test_https_config.py`
- 启动服务: `./start-https.sh`
