### Background
* [Host, Port](http://www.runoob.com/java/java-url-processing.html)
* 下圖說明為何我們一般網頁不會看到 Port ，是因為中間有 NGINX 做媒介。Nginx 主要功用在反向代理，負載平衡器 和 HTTP快取
![Nginx](static\nginx-sails.png)

### Reference website
* [Flask 的中文 QuickStart](http://docs.jinkan.org/docs/flask/quickstart.html)

### 使用方式
1. 在 cmd 下，透過下面指令開啟伺服器
```bash
python note_1.py
```
2. 用瀏覽器輸入以下網址，可看到 initial 字串
> http://localhost:5000

3. 再用瀏覽器輸入以下網址，可看到 another 字串
> http://localhost:5000/another