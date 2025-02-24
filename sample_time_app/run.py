from flask import Flask
from datetime import datetime
import pytz

# 指定你需要的时区，例如 "Asia/Shanghai"
tz = pytz.timezone("America/New_York")

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
    # 指定纽约所在时区
    ny_tz = pytz.timezone("America/New_York")
    
    # 获取纽约当前时间
    ny_time = datetime.now(ny_tz)
    
    # 使用 str.format() 代替 f-string
    return "Current time in New York: {}".format(ny_time)
app.run(host='0.0.0.0',
        port=8080,
        debug=True)
