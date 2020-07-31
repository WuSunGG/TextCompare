from os import path

from bs4 import BeautifulSoup


class html2txt:

    def htmlcontent(self,htmlcontent):
        """
        trans html content to plain content
        :param htmlcontent:
        :return:
        """
        try:
            soup = BeautifulSoup(htmlcontent, "lxml")
            return (soup.get_text())
        except Exception as e:
            return False
