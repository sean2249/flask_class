from flask import Flask, url_for, render_template, request
# 這堂會教大家
# 1. 如何在網頁呈現自己的圖片或其他多媒體 (static, template)
# 2. 建立 html 表單 (template)
# 3. 回收表單 (flask)

app = Flask(__name__)
# 在 server 運行時，若 template 有修改時，預設是不會自動更新，故需加入下兩行程式來更新
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

navs_inlist = ['main', 'an', 
    'internal_link', 'external_link', 'all_routes',
    'render', 'listNav']
navs_indict = {
    'class1': ['main', 'an'],
    'class2': ['internal_link', 'external_link', 'all_routes'],
    'class3': ['render', 'listNav', 'dictNav', 'sortDictNav', 'hrefDictNav'],
    'class4': ['imgs', 'batchImgs', 'getForm', 'getRequest', 'postForm', 'postRequest']

}
# -- Class 4
# 將 navigation page 利到 main page
@app.route('/')
def main():
    return render_template('nav.html', 
        navs=sorted(navs_indict.items()))

# 注意：因瀏覽器為了加速，會儲存之前讀過的內容，即為 cache
# 故若發現結果不是你想像中的，可嘗試用瀏覽器的無痕視窗來檢視
@app.route('/imgs')
def imgs():
    return render_template('imgs.html')

# 利用 os.listdir 取出 static 中所有圖片，並利用 os.path.splitext 濾掉副檔名
# 然後傳入到 template 中，產生 gallery
@app.route('/batchImgs')
def batchImgs():
    import os     
    catDict = {os.path.splitext(f)[0]:f 
                for f in os.listdir('static')}
    return render_template('batchImgs.html', pics=catDict)

@app.route('/getForm')
def getForm():
    return render_template('getForm.html')

# 因為是用 GET 的方式來傳，所以你會看到網址包含了表單填的資訊
# 可看到底下多一個 methods=['GET']，代表這個route只接受GET的內容，預設的methods是全部
# 一定要看的網站：https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request
@app.route('/getRequest', methods=['GET'])
def getRequest():
    # 透過 request.args 來取得 GET 的資訊， request.args.get(<key>, <default value if key not found>)
    username = request.args.get('username')
    nickname = request.args.get('nickname')
    # IF NICKNAME not found, try to get Key=smart in html, but failed, default value=POOP!!
    if len(nickname)==0:
        nickname = request.args.get('smart', 'POOP')
    return 'Hi {}. May I call u {}'.format(username, nickname)

# 改用 post 的方式來傳遞
@app.route('/postForm')
def postForm():
    return render_template('postForm.html')
    
# 因用 post 傳，可發現網址變乾淨了~
@app.route('/postRequest', methods=['POST'])
def postRequest():
    username = request.form.get('username')
    nickname = request.form.get('nickname')
    if len(nickname)==0:
        nickname = request.args.get('smart', 'POOP')
    return 'Hi {}. May I call u {}'.format(username, nickname)

# -- Class 3
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
@app.route('/another')
def an():
    return 'another'
##-------##



if __name__ == '__main__':
    app.run(debug=True)
