#!/usr/bin/env python3
"""
测试 HTTPS 配置
"""

import ssl
import socket
import urllib3
from pathlib import Path

# 禁用 SSL 警告（仅用于测试）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def test_certificate_exists():
    """测试证书文件是否存在"""
    cert_path = Path('certs/cert.pem')
    key_path = Path('certs/key.pem')

    print("📋 检查证书文件...")

    if cert_path.exists() and key_path.exists():
        print(f"  ✓ 证书文件存在: {cert_path.stat().st_size} bytes")
        print(f"  ✓ 私钥文件存在: {key_path.stat().st_size} bytes")
        return True
    else:
        print(f"  ✗ 证书文件不存在")
        return False


def test_certificate_validity():
    """测试证书有效性"""
    print("\n📋 验证证书有效性...")

    try:
        # 加载证书
        cert_dict = ssl._ssl._test_decode_cert('certs/cert.pem')

        print(f"  ✓ 主题: {cert_dict.get('subject', [])}")
        print(f"  ✓ 颁发者: {cert_dict.get('issuer', [])}")
        print(f"  ✓ 有效期: {cert_dict.get('notAfter', 'N/A')}")

        return True
    except Exception as e:
        print(f"  ✗ 证书验证失败: {e}")
        return False


def test_port_configuration():
    """测试端口配置"""
    print("\n📋 检查端口配置...")

    host = '172.16.48.112'
    port = 15032

    try:
        # 尝试连接端口（可能尚未启动）
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:
            print(f"  ✓ 端口 {port} 在 {host} 上可访问")
        else:
            print(f"  ℹ 端口 {port} 在 {host} 上尚未监听（正常，服务器未启动）")

        return True
    except Exception as e:
        print(f"  ✗ 端口检查失败: {e}")
        return False


def test_app_config():
    """测试应用配置"""
    print("\n📋 检查应用配置...")

    try:
        with open('app.py', 'r') as f:
            content = f.read()

            checks = {
                '172.16.48.112': False,
                '15032': False,
                'ssl_context': False,
                'certs/cert.pem': False,
                'certs/key.pem': False
            }

            for key in checks.keys():
                if key in content:
                    checks[key] = True

            all_ok = all(checks.values())

            if all_ok:
                print("  ✓ 主机配置: 172.16.48.112")
                print("  ✓ 端口配置: 15032")
                print("  ✓ SSL 配置: 已启用")
                print("  ✓ 证书路径: 正确")
            else:
                for key, status in checks.items():
                    if not status:
                        print(f"  ✗ 配置缺失: {key}")

            return all_ok

    except Exception as e:
        print(f"  ✗ 配置检查失败: {e}")
        return False


def main():
    """主测试函数"""
    print("=" * 50)
    print("  HTTPS 配置测试")
    print("=" * 50)

    results = []

    # 运行测试
    results.append(("证书文件", test_certificate_exists()))
    results.append(("证书有效性", test_certificate_validity()))
    results.append(("端口配置", test_port_configuration()))
    results.append(("应用配置", test_app_config()))

    # 汇总结果
    print("\n" + "=" * 50)
    print("  测试结果汇总")
    print("=" * 50)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✓ 通过" if result else "✗ 失败"
        print(f"{name}: {status}")

    print("\n" + "=" * 50)
    print(f"总计: {passed}/{total} 测试通过")
    print("=" * 50)

    if passed == total:
        print("\n✅ 所有配置检查通过！")
        print("\n🚀 启动服务器:")
        print("   ./start-https.sh")
        print("\n🌐 访问地址:")
        print("   https://172.16.48.112:15032")
        print("\n⚠️  浏览器会显示安全警告（自签名证书），这是正常的")
    else:
        print("\n❌ 部分配置检查失败，请检查上述错误")


if __name__ == '__main__':
    main()
