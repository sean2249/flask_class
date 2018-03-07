from flask import Flask

# 建立一個 Flask 物件，來容納接下去的 route 或擴充。
app = Flask(__name__)

# 從上方的 Flask 物件，建立 Route 裝飾器來告知怎樣的 URL 會觸發此函數
# 如下即為 Domain
@app.route('/')
def main():
    # 可回傳 String，之後會有更多的回傳方式 (ex.render_template, jsonify)
    return 'initial'

# 建立另一個Route裝飾器 another ，含有 bug
@app.route('/another')
def an():
    return another

# 使伺服器不在別支程式 import 時啟動
if __name__ == '__main__':
    # 預設為 host=localhost, port=5000
    # app.run()
    
    # 但為了開發我們通常會額外開啟 debug 模式
    app.run(debug=True)
