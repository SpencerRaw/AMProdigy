# 使用官方的 Python 3.11 镜像
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 复制当前目录的所有文件到工作目录
COPY . /app

# 安装指定版本的 peptides 库
RUN pip install fastapi uvicorn peptides==0.3.4

# 暴露端口
EXPOSE 8000

# 运行 Uvicorn 服务器
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
