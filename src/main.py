#!/usr/bin/env python3
"""
GitHub Action - Python Custom Action
A reusable GitHub Action written in Python (Docker mode)
"""

import os
import sys
import argparse
from pathlib import Path

def main():
    """Main function for the GitHub Action"""
    
    # 在Docker模式下，GitHub Actions会自动将inputs设置为环境变量
    # 格式是 INPUT_<参数名> (大写)
    message = os.getenv('INPUT_MESSAGE') or '111111111111111111Hello from Python custom action!'
    
    try:
        # 执行主要逻辑
        print('🚀 Running Python custom action (Docker mode)...')
        print(f'📝 Message: {message}')
        
        # 处理消息
        result = f'Processed: {message}'
        
        # 设置GitHub Action输出
        # GitHub Actions需要将输出写入到特定文件
        # output_file = os.getenv('GITHUB_OUTPUT', 'github_output.txt')
        
        # with open(output_file, 'a') as f:
        #     f.write(f'result={result}\n')
        
        # 打印结果
        print(f'✅ Action completed successfully!')
        print(f'📤 Result: {result}')
        
        # 打印设置输出信息
        print(f'::set-output name=result::{result}')
        
    except Exception as error:
        # 设置失败状态
        print(f'❌ Error: {error}', file=sys.stderr)
        print('::error::Action failed!')
        sys.exit(1)

if __name__ == '__main__':
    main()