# -*- coding: utf-8 -*
import webbrowser
class Movie():
    '''定义Python类Movie'''
    def __init__(self, movie_title, poster_image, trailer):
        '''__init__是类Movie的构造函数，传入参数电影标题movie_title，封面图片地址poster_image，预览视频地址trailer，
        最终生成实例的title，poster_image_url，trailer_youtube_url属性'''
        self.title=movie_title
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer
    def show_trailer(self):
        '''show_trailer函数调用Python内置模块webbrowser的open方法来打开浏览器'''
        webbrowser.open(self.trailer_youtube_url)

