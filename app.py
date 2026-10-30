from flask import Flask, jsonify
import pymysql
import pymysql.cursors

app = Flask(__name__)
app.json.ensure_ascii = False   # 加這一行，關閉ASCII強制轉義

def get_connection():
    return pymysql.connect(
        host="host.docker.internal",  # 特殊DNS 讓容器連回主機
        port=3306,
        database="classicmodels",
        user="root",
        password="1234"
    )

@app.route("/products")
def get_products():
    conn = get_connection()
    # DictCursor讓查詢結果直接是dict格式 方便轉JSON
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM products LIMIT 10;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)


