# 使用基础镜像（Python 3.8+）
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    libatlas-base-dev \
    liblapack-dev \
    libopenblas-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

    RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*
# 复制项目所有文件到容器
COPY . .

# 安装依赖项
RUN pip install --no-cache-dir -r requirements.txt

# 设置默认执行命令
CMD ["python", "calculate_scores_real_videos"]

