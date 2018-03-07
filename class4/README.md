### Form passing
1. action: the location u want to send
2. method: GET/POST [Difference between GET/POST](https://blog.toright.com/posts/1203/%E6%B7%BA%E8%AB%87-http-method%EF%BC%9A%E8%A1%A8%E5%96%AE%E4%B8%AD%E7%9A%84-get-%E8%88%87-post-%E6%9C%89%E4%BB%80%E9%BA%BC%E5%B7%AE%E5%88%A5%EF%BC%9F.html)

## [Get data in flask request](https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request)
```python
# POST
request.form.get()
# GET
request.args.get()
# HEADER
request.header.get()
```
### Reference website
* [Reload Flask app when template file changes](https://stackoverflow.com/questions/9508667/reload-flask-app-when-template-file-changes)
* Form 介紹
    * http://www.wibibi.com/info.php?tid=188
    * https://developer.mozilla.org/zh-TW/docs/Learn/HTML/Forms/How_to_structure_an_HTML_form

