
import urllib.request as req
import warnings
import bs4
from fpdf import FPDF


class downloadNovel():
    
    def __init__(self,url,ua):
        self.url=url
        self.request=req.Request(url,headers={"User-Agent": ua})
        self.context = self.htmlContext()
        self.root= self.getRoot()

    def htmlContext(self):
        with req.urlopen(self.request) as response:
            return response.read()

    def getRoot(self):
        return bs4.BeautifulSoup(self.context,"html.parser")

    def getTitle(self):
        return self.root.title.string
    
    def getContent(self):
        content = self.root.find("p", class_="content")
        return content.strings
    
    def printContent(self):
        content = self.getContent()
        for string in content:
            print(string)

    def download(self):
        self.title=self.getTitle()
        print(self.title + " 下載中")
        content=self.getContent()

        pdf = FPDF()
        pdf.add_page()


        pdf.add_font('034', '', '034.ttf', uni=True)
        pdf.set_font('034', '', 14)
        pdf.write(5, self.title+'\n'+'\n')

        for string in content:
            pdf.add_font('064', '', '064.ttf', uni=True)
            pdf.set_font('064', '', 10)
            pdf.write(5, string)

        pdf.output(self.title+".pdf")

url= [
      "https://8book.com/readbook/15/118435/23576.html",
      "https://8book.com/readbook/15/118435/23578.html",
      "https://8book.com/readbook/15/118435/23579.html",
      "https://8book.com/readbook/15/118435/23580.html",
      "https://8book.com/readbook/15/118435/23581.html",
      "https://8book.com/readbook/15/118435/23582.html"]

ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"

'''
novel = downloadNovel(url,ua)
novel.htmlContext()
root=novel.getRoot()
print(novel.getString(root.title))
content=root.find("p", class_="content")
for string in content.strings:
    print(string)
'''

for i in range(len(url)):
    novel = downloadNovel(url[i],ua)
    novel.download()



