#套件庫
from flask import Flask, jsonify
import psycopg2
import psycopg2.extras

#啟動
app = Flask(__name__)
app.json.ensure_ascii = False   # 加這一行，關閉ASCII強制轉義

#連線到資料庫
def get_connection():
    return psycopg2.connect(
        host="host.docker.internal",  # 特殊DNS 讓容器連回主機
        port=5433,
        dbname="shin02",
        user="pguser",
        password="pgUser567"
    )

#取得資料 (前10筆)
@app.route("/products")
def get_products():
    conn = get_connection()
    # RealDictCursor讓查詢結果直接是dict格式 方便轉JSON
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM products LIMIT 10;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

#程式進入點
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)


    