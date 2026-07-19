#來自哪個image
#FROM 一定要寫在第一行
FROM python:3.11-slim

#進入容器的工作目錄
WORKDIR /app

#預設安裝的套件
RUN pip install --no-cache-dir flask psycopg2-binary --break-system-packages

#作者
LABEL maintainer="stevenIspan"

#第一個.  代表當下目錄的路徑    第二個. 代表要放到容器內的預設位置
#COPY . .

#宣告一個資料夾作為對外的空間
VOLUME [ "/app/logs" ]

#對外的pot
EXPOSE 3000

#CMD要執行的打在最後
#CMD [ "python","app.py" ]