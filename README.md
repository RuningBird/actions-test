# My Python Custom GitHub Action

一个用Python编写的可重用GitHub Action（Composite模式），可以在其他workflow中被调用。

## 功能特性

- ✅ Python实现的GitHub Action（Composite模式）
- ✅ 接收自定义消息参数
- ✅ 处理并返回处理结果
- ✅ 无需Docker，部署更简单
- ✅ 完整的错误处理机制
- ✅ 易于集成到其他workflows

## 输入参数

| 参数 | 描述 | 必需 | 默认值 |
|------|------|------|--------|
| `message` | 要处理的消息 | 否 | `"Hello from custom action!"` |

## 输出参数

| 参数 | 描述 |
|------|------|
| `result` | 处理后的结果消息 |

## Composite模式优势

- 🚀 **更快启动**：无需构建Docker镜像
- 🔧 **更简单维护**：不需要Dockerfile和镜像管理
- 💰 **更少资源**：直接运行Python脚本，资源占用更少
- 🛠️ **更容易调试**：可以在GitHub Actions中直接查看Python输出

## 使用方法

### 1. 在workflow中使用 (GitHub Marketplace方式)

```yaml
name: Use Custom Action

on:
  workflow_dispatch:

jobs:
  use-action:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Use custom action
        uses: YOUR_USERNAME/YOUR_REPO_NAME@v1.0.0
        with:
          message: "Hello from custom action!"
```

### 2. 在workflow中使用 (本地路径方式)

```yaml
name: Test Local Action

on:
  workflow_dispatch:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Use local action
        uses: ./
        with:
          message: "Testing local action"
```

### 3. 获取action输出结果

```yaml
- name: Use custom action
  id: custom
  uses: YOUR_USERNAME/YOUR_REPO_NAME@v1.0.0
  with:
    message: "Hello World"

- name: Get output
  run: echo "Result: ${{ steps.custom.outputs.result }}"
```

## 开发环境设置

### 1. 克隆仓库

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. 安装Python依赖 (可选)

```bash
# 如果需要额外的Python包
pip install -r requirements.txt
```

### 3. 测试action

```bash
# 直接运行Python脚本
python3 src/main.py
```

## 目录结构

```
├── .github/
│   └── workflows/
│       ├── test-action.yml      # 测试workflow
│       └── blank.yml            # 原始workflow
├── src/
│   └── main.py                  # Python Action入口文件
├── action.yml                   # Action元数据（Composite模式）
├── requirements.txt             # Python依赖
└── README.md                    # 说明文档
```

## 发布版本

1. 更新 `action.yml` 中的版本信息 (可选)
2. 创建Git标签: `git tag v1.0.0`
3. 推送标签: `git push origin v1.0.0`

## 注意事项

- 确保每次发布前都要运行 `npm run build`
- 更新 `action.yml` 中的版本号引用
- 在GitHub Marketplace中发布需要经过审核

## 许可证

MIT License

## 贡献

欢迎提交Pull Request和Issue！

## 支持

如果遇到问题，请查看 [Issues](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/issues) 页面。