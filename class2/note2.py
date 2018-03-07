from flask import Flask, url_for
# url_for 功用為呈現 各 route 函數 的進入 url
# Input 函數的名稱（不是我們在 route 裡填入的網址）
# Ouput 對應函數的 URL

app = Flask(__name__)

@app.route('/')
def main():
    return 'initial'

@app.route('/another')
def an():
    return 'another'

# Internal link, without host name
@app.route('/internal_link')
def internal_link():
    return url_for('main')

# External link, with hostname.
@app.route('/external_link')
def external_link():
    return url_for('main', _external=True, a='adsf')

# 導入一些 WEB 的元件，建立一個最基本的導覽頁面~
@app.route('/all_routes')
def all_routes():
    return '<a href=\'{m}\'>{m}</a><br><a href=\'{an}\'>Another</a>'.format(m=url_for('main'), an=url_for('an'))

if __name__ == '__main__':
    app.run(debug=True)
