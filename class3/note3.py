from flask import Flask, url_for, render_template
# 這時候你會發現你要建立個最基本的導覽頁面，就需要寫很難看的 string format，實在很麻煩
# 因此這堂講的是新函數 render_template ，我們可以透過此函數將我們所需要的參數扔進我們預設定好的網頁樣本中
# Input 

app = Flask(__name__)

navs_inlist = ['main', 'an', 
    'internal_link', 'external_link', 'all_routes',
    'render', 'listNav']
navs_indict = {
    'class1': ['main', 'an'],
    'class2': ['internal_link', 'external_link', 'all_routes'],
    'class3': ['render', 'listNav', 'dictNav', 'sortDictNav', 'hrefDictNav']

}
# 單純的顯示網頁的模組
@app.route('/render')
def render():
    return render_template('nopara.html')

# 假設你指定的參數有對應到 template 裡的參數 
# render_template 可以帶入多個參數到網頁模組 (template)
# 網頁會藉由 flask.render_template 傳遞的參數可以顯示出來
@app.route('/listNav')
def listNav():
    return render_template('navList.html', lst=navs_inlist)

# 傳入 dictionary ，並做多層的顯示（template-view）
@app.route('/dictNav')
def dictNav():
    return render_template('nav.html', navs=navs_indict)

# 因 dict.items() 會隨機取樣，所以先做個 sorted 確保 class 的順序 
@app.route('/sortDictNav')
def sortDictNav():
    return render_template('nav.html', navs=sorted(navs_indict.items()))

# 在 template 中可利用 url_for 產生連結網站，使 navigation 完成！
@app.route('/hrefDictNav')
def hrefDictNav():
    return render_template('nav.html', 
            navs=sorted(navs_indict.items()))

#----- Class 2
@app.route('/internal_link')
def internal_link():
    return url_for('main')

@app.route('/external_link')
def external_link():
    return url_for('main', _external=True)

@app.route('/all_routes')
def all_routes():
    return '<a href=\'{m}\'>{m}</a><br><a href=\'{an}\'>Another</a>'.format(m=url_for('main'), an=url_for('an'))

#---- Class 1
@app.route('/')
def main():
    return 'initial'

@app.route('/another')
def an():
    return 'another'
##-------##



if __name__ == '__main__':
    app.run(debug=True)
