# 使用官方Python镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /workspace

# 复制源代码
COPY src/ ./src/
COPY requirements.txt ./

# 安装Python依赖 (如果有的话)
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# 设置入口点
ENTRYPOINT ["python3", "src/main.py"]