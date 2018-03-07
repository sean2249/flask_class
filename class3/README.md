## Template 語法- Jinja2
* Jinja2 語法跟 html 有像相似，但主要的功能為接收python產出的資料（即為 controller -> view)
* [Jinja 中文文檔](http://docs.jinkan.org/docs/jinja2/)

### Jinja2 極簡易介紹
* {{ }} 這個是參數，template 會根據 render_template 傳遞的參數來產生對應的網頁原始檔
* {# #} 這個是註解 
* {% %} 這個是類似 function (ex. for, if-else, while, def...)
    * 注意：function 最後要有 end，如下
    ```
    {% for i in lst %}
        {{ i }}
    {% endfor %}
    ```

