# coding:utf-8
import urlparse,__init__
import re
import urllib
from bs4 import BeautifulSoup
class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls=set()
        # /p/5477186663
        links = soup.find_all('a',href=re.compile(r"/p/\d+"))
        head_url='http://tieba.baidu.com'
        for link in links:
            new_url = link['href']
            new_full_url=urlparse.urljoin(head_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    @staticmethod
    def save_image(self,img_list,i):
        x = 0
        for img_url in img_list:
            print img_url
            location = __init__.save_dir + "%s%s.jpg"
            urllib.urlretrieve(img_url, location % (i, x))
            x += 1

    @staticmethod
    def _get_img_list(self,html_cont):
        reg = r'src="(http.?://imgsrc.baidu.com/.*?\.jpg)"'
        img_re = re.compile(reg)
        html_d = html_cont.decode('utf-8')
        img_list = img_re.findall(html_d)
        return img_list

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        img_list = self._get_img_list(self, html_cont)
        self.save_image(self, img_list, __init__.count)
        __init__.count = __init__.count + 1
        return new_urls



    