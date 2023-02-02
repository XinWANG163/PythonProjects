# 使用Flask框架
# pip install Flask
import random

from flask import Flask, render_template
# 构建app
app = Flask(__name__)

heroList = [
        '司空震','蒙恬','阿古朵','夏洛特','澜','镜',
        '蒙犽','鲁班大师','西施','马超','曜','云中君',
        '瑶','盘古','猪八戒','嫦娥','上官婉儿','李信',
        '沈梦溪','伽罗','盾山','司马懿','孙策','元歌',
        '米莱狄','狂铁','弈星','裴擒虎','杨玉环','公孙离',
        '明世隐','女娲','梦奇','苏烈','百里玄策','百里守约',
        '铠','鬼谷子','干将莫邪','东皇太一','大乔','黄忠',
        '诸葛亮','哪吒','太乙真人','蔡文姬','雅典娜','杨戬',
        '成吉思汗','钟馗','虞姬','李元芳','张飞','刘备',
        '后羿','牛魔','孙悟空','亚瑟','橘右京','娜可露露',
        '不知火舞','张良','花木兰','兰陵王','王昭君',
        '韩信','刘邦','姜子牙','露娜','程咬金','安琪拉',
        '貂蝉','关羽','老夫子','武则天','项羽',
        '达摩','狄仁杰','马可波罗','李白','宫本武藏','典韦'
]

@app.route('/index')
def index():
    return render_template('index.html',heroList = heroList)

@app.route('/tiresort')
def tiresort():
    l = len(heroList)
    n = random.randint(0,l-1)
    return render_template('tiresort.html',name = heroList[n])
# 运行程序
app.run(debug=True)