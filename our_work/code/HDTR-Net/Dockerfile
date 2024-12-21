# 使用基础镜像（Python 3.8+）
FROM python:3.8-slim

# 安装系统依赖，包括 libGL 库
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*
    
# 设置工作目录
WORKDIR /app

# 复制项目所有文件到容器
COPY . .

# 安装依赖项
RUN pip install --no-cache-dir -r requirements.txt

# 设置默认执行命令（执行 inference.py）
CMD ["python", "inference.py"]
