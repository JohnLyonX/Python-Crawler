import threading

import requests
from lxml import etree
import os

res = requests.get(
    "https://www.pkdoutu.com/article/detail/9629715",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    },
)
tree = etree.HTML(res.text)
par = tree.xpath("//div[@class='artile_des']")
print(par)


def download_img(get_url):
    res_img = requests.get(get_url)
    img_name = os.path.basename(get_url)
    path = os.path.join('imgs', img_name)
    if not os.path.exists('imgs'):
        os.mkdir('imgs')
    with open(path, 'wb') as f:
        for i in res_img.iter_content():
            f.write(i)


list_img = []
for item in par:
    src = item.xpath('.//@src')[0]
    threading.Thread(target=download_img, args=(src,)).start()