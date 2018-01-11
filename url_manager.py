# coding:utf-8
class UrlManager(object):
    def __init__(self):
        self.new_urls=set()  #正在爬取的
        self.old_urls=set()  #已经爬取的

#判断该url是否是新的url
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

#增加新的urls
    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

#检测是否还有待爬取链接
    def has_new_url(self):
        return len(self.new_urls) != 0

#获取新的url，并将其放入已访问url
    def get_new_url(self):
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
