#!/usr/bin/env python3
"""
Python GitHub Action
Composite mode
"""

import os

def main():
    """Main function for the GitHub Action"""
    
    # 在Docker模式下，GitHub Actions会自动将inputs设置为环境变量
    # 格式是 INPUT_<参数名> (大写)
    message = os.getenv('INPUT_MESSAGE') or 'Hello from Python custom action!'
    
    # 执行主要逻辑
    print('🚀 Running Python custom action (Composite mode)...')
    print(f'📝 Message: {message}')
    
    # 处理消息
    result = f'Processed: {message}'
    print(f'📤 Result: {result}')
    
    # Output result for GitHub Actions (Composite mode - will be captured by shell)
    print(result)
    print('✅ Action completed successfully!')

if __name__ == '__main__':
    main()