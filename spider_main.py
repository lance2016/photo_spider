# coding:utf8
import os

import html_downloader,html_outputer,html_parser,url_manager,__init__


class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outpyter=html_outputer.HtmlOutputer()

    def craw(self, root_url):
        try:
            count=1
            self.urls.add_new_url(root_url)
            while self.urls.has_new_url():
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' %(count,new_url)     #提示输出
                html_cont = self.downloader.download(new_url)
                new_urls = self.parser.parse(new_url,html_cont)
                print new_urls
                self.urls.add_new_urls(new_urls)

                if count == 50:
                    break
                count = count + 1
        except:
            print 'craw failed'

        self.outpyter.output_html()
    pass


if __name__=='__main__':
    if not os.path.exists(__init__.save_dir):
        os.mkdir(__init__.save_dir)
    obj_spider=SpiderMain()
    obj_spider.craw(__init__.root_url)