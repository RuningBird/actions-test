#!/usr/bin/env python3
"""
Python GitHub Action (Composite)
兼容我们的 Runner 和 GitHub Actions：
- 输入通过环境变量 INPUT_MESSAGE 传递
- 输出可选写入 GITHUB_OUTPUT（若存在）
"""

import os
import sys
import argparse
from pathlib import Path

def main():
    message = os.getenv('MESSAGE') or 'Hello from Python custom action!'
    try:
        print('🚀 Running Python custom action (Composite mode)...')
        print(f'📝 Message: {message}')
        # requests 示例：调用一个公共 API
        try:
            import requests
            r = requests.get('https://httpbin.org/get', timeout=5)
            status = r.status_code
            print(f'🌐 requests status={status}')
        except Exception as e:
            print(f'⚠️ requests import/call failed: {e}')
        result = f'Processed: {message}'
        print(f'📤 Result: {result}')
        out = os.getenv('GITHUB_OUTPUT')
        if out:
            try:
                with open(out, 'a', encoding='utf-8') as f:
                    f.write(f'result={result}\n')
            except Exception:
                pass
        print('✅ Action completed successfully!')
    except Exception as error:
        print(f'❌ Error: {error}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
