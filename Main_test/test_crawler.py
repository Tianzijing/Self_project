import os
import re
import requests
from urllib.request import urlretrieve


url = "http://www.pearvideo.com/category_1"
http = requests.get(url)
http.encoding = http.apparent_encoding
http_text = http.text
# print(http_test)
find_text = '<a href="(.*?)" class="vervideo-lilink actplay">'
video_list_name = re.findall(find_text, http_text)
# print(len(video_list_name))
# print(video_list_name)

for i in video_list_name:
    video_url = "http://www.pearvideo.com/" + i
    print(video_url)
    video_http = requests.get(video_url)
    # video_http.encoding = video_http.apparent_encoding
    video_http_text = video_http.text
    # print(video_http_text)
    find_video_url = 'ldUrl="",srcUrl="(.*?)",vdoUrl=srcUrl'
    find_video_title = '<h1 class="video-tt">(.*?)</h1>'
    video_plan_url = re.findall(find_video_url, video_http_text)
    video_plan_title = re.findall(find_video_title, video_http_text)
    # print(video_plan_title)
    video_text = video_plan_title[0].replace(
        '"',
        "_").replace(
        ',',
        "，").replace(
            ':',
        "：")
    print("正在下载视频：{}".format(video_text))

    # 所在目录上一级 + 文件夹名称 如果不存在就创建
    path_save = os.path.abspath(os.path.join(os.getcwd(), "..")) + r"\video"
    if not os.path.exists(path_save):
        os.mkdir(path_save)
    path = path_save + "/%s.mp4" % video_text
    print(video_plan_url[0], "\n")
    try:
        urlretrieve(video_plan_url[0], path)
    except BaseException:
        print("下载失败")
