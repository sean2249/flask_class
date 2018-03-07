### Function 
* Usage
```python
url_for(<function name>, <request-get parms>)

## Example
>>> @app.route('/')
... def main():
...     return 'dfdf'
>>> url_for('main', _external=True)
... http://localhost:5000/
>>> url_for('main', _external=True, a='123')
... http://localhost:5000/?a=123
```
* 關於 request 裡的 get, post 會待入到 flask 中 

### Reference website 
* [Flask.url_for](http://flask.pocoo.org/docs/0.12/api/#flask.url_for)
