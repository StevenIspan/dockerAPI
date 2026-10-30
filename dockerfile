# 1. 指定基礎映像
FROM python:3.11-slim
# 2. 中繼資料標籤，用來記錄這個Image的資訊
LABEL maintainer="stevenispan"
# 3. 設定容器內的工作目錄
WORKDIR /app
# 4. 直接安裝所需套件
RUN pip install --no-cache-dir flask pymysql cryptography --break-system-packages
# 5. 複製程式碼進容器
COPY . .
# 6. 宣告一個持久化用的資料夾（例如放程式log）
VOLUME ["/app/logs"]
# 7. 宣告容器對外開放的埠（僅供說明用途，不會真的開埠）
EXPOSE 3000
# 8. 容器啟動時執行的指令
CMD ["python", "app.py"]
